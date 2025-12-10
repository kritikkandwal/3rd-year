from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import json
import joblib
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any

# --- Configuration ---
OPTIONS_FILE = "State_data.json"
MODEL_FILE = "model/crop_yield_pipeline.joblib"

# --- Data Models (Using BaseModel for data validation in the POST request) ---
class PredictInput(BaseModel):
    crop: str
    state_name: str
    season: str
    area: float
    rainfall: float  # Raw rainfall input (in mm)

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# --- FastAPI App Initialization & Middleware ---
app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Global Artifacts ---
FRONTEND_OPTIONS_CACHE: Optional[Dict[str, Dict[str, List[str]]]] = None
XGB_MODEL = None
PREPROCESSOR = None
CROP_MEANS = None
TRAIN_COLUMNS = None
MODEL_LOADED = False

# --------------------------
# Utility: make objects JSON safe
# --------------------------
def to_json_friendly(x: Any) -> Any:
    """
    Convert numpy scalars/arrays/pandas types to JSON-serializable Python types.
    """
    # numpy ndarray -> list (or scalar if single)
    if isinstance(x, np.ndarray):
        if x.size == 1:
            return float(x.item())
        return x.tolist()
    # numpy scalar
    if isinstance(x, (np.generic,)):
        return float(x.item())
    # pandas types with tolist()
    if hasattr(x, "tolist") and not isinstance(x, (str, bytes, dict, list)):
        try:
            t = x.tolist()
            # prefer scalar if single element
            if isinstance(t, (list, tuple)) and len(t) == 1:
                return t[0]
            return t
        except Exception:
            pass
    # default (assume already JSON compatible)
    return x

# --------------------------
# Prediction logic
# --------------------------
def run_prediction_logic(crop: str, state: str, season: str, area: float, rainfall: float) -> float:
    """
    Transform the input using PREPROCESSOR and predict using XGB_MODEL.
    Returns a native Python float for the predicted yield (Tonnes/ha).
    """
    global TRAIN_COLUMNS, PREPROCESSOR, XGB_MODEL, CROP_MEANS

    if TRAIN_COLUMNS is None or PREPROCESSOR is None or XGB_MODEL is None or CROP_MEANS is None:
        raise RuntimeError("Model artifacts are not loaded.")

    # 1. Create base input DataFrame with zeros for all training columns
    input_data = pd.DataFrame(0, index=[0], columns=TRAIN_COLUMNS)

    # 2. Numerical features (must match training pipeline expected column names)
    # Note: The original code used 'Area' and 'Rainfall' column names.
    # Make sure TRAIN_COLUMNS contains those names exactly; else adapt.
    if "Area" in input_data.columns:
        input_data["Area"] = float(area)
    else:
        # try lowercase fallback
        if "area" in input_data.columns:
            input_data["area"] = float(area)

    if "Rainfall" in input_data.columns:
        input_data["Rainfall"] = float(rainfall)
    else:
        if "rainfall" in input_data.columns:
            input_data["rainfall"] = float(rainfall)

    # 3. Target (mean) encoding for crop
    # Use raw crop string as key lookup (backend CROP_MEANS should use same naming)
    global_mean_yield = float(np.mean(list(CROP_MEANS.values()))) if CROP_MEANS else 0.0
    crop_encoded_key = crop.strip()
    input_data["Crop_Encoded"] = float(CROP_MEANS.get(crop_encoded_key, global_mean_yield))

    # 4. One-hot style encoding for state & season if columns exist
    state_col = f"State_Name_{state}".lower().replace(" ", "_")
    # TRAIN_COLUMNS may contain lowercase column names; check both
    # Check candidates to set value to 1 if present
    if state_col in input_data.columns:
        input_data[state_col] = 1
    else:
        # attempt to match case-insensitively
        for col in input_data.columns:
            if col.lower() == state_col:
                input_data[col] = 1
                break

    season_col = f"Season_{season}".lower().strip()
    if season_col in input_data.columns:
        input_data[season_col] = 1
    else:
        for col in input_data.columns:
            if col.lower() == season_col:
                input_data[col] = 1
                break

    # 5. Transform and predict
    # PREPROCESSOR.transform expects the exact set of columns passed in TRAIN_COLUMNS order
    try:
        transformed = PREPROCESSOR.transform(input_data[TRAIN_COLUMNS])
    except Exception as e:
        # If preprocess fails, raise a helpful error
        logging.exception("Preprocessor.transform failed: %s", e)
        raise

    try:
        prediction = XGB_MODEL.predict(transformed)
    except Exception as e:
        logging.exception("Model prediction failed: %s", e)
        raise

    # prediction may be numpy array/scalar; return native float
    pred0 = prediction[0] if hasattr(prediction, "__len__") else prediction
    pred_native = to_json_friendly(pred0)
    try:
        return float(pred_native)
    except Exception as e:
        logging.exception("Failed to coerce prediction to float: %s (value repr=%r)", e, pred_native)
        raise

# --------------------------
# Startup: load artifacts and options
# --------------------------
@app.on_event("startup")
async def load_data_and_model():
    global FRONTEND_OPTIONS_CACHE, XGB_MODEL, PREPROCESSOR, CROP_MEANS, TRAIN_COLUMNS, MODEL_LOADED

    # Load options file
    try:
        with open(OPTIONS_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
            # Normalize keys to lowercase so lookups are consistent
            FRONTEND_OPTIONS_CACHE = {k.lower(): v for k, v in raw.items()}
        logging.info("Successfully loaded frontend options from %s.", OPTIONS_FILE)
    except FileNotFoundError:
        logging.error("FATAL: Options file '%s' not found. Ensure you run the JSON generation script.", OPTIONS_FILE)
    except Exception as e:
        logging.exception("FATAL: Error reading or parsing options JSON: %s", e)

    # Load model artifacts
    try:
        artifacts = joblib.load(MODEL_FILE)
        # Expecting artifact keys: 'model', 'preprocessor', 'crop_means', 'train_columns'
        XGB_MODEL = artifacts.get("model") or artifacts.get("xgb_model") or artifacts.get("pipeline")
        PREPROCESSOR = artifacts.get("preprocessor") or artifacts.get("preprocessor_pipeline")
        CROP_MEANS = artifacts.get("crop_means", {})
        TRAIN_COLUMNS = artifacts.get("train_columns") or artifacts.get("columns")
        MODEL_LOADED = True
        logging.info("Prediction pipeline loaded successfully from %s.", MODEL_FILE)
    except FileNotFoundError:
        logging.error("FATAL: Model file '%s' not found. Prediction endpoint will be disabled.", MODEL_FILE)
    except Exception as e:
        logging.exception("FATAL: Error loading model artifacts: %s", e)

# --------------------------
# API Endpoints
# --------------------------
@app.get("/api/options")
async def get_state_options():
    if FRONTEND_OPTIONS_CACHE is None:
        raise HTTPException(status_code=503, detail=f"Options data is unavailable. Check server logs for {OPTIONS_FILE} loading errors.")
    states = sorted(FRONTEND_OPTIONS_CACHE.keys())
    logging.info("Serving list of available states.")
    return {"states": states}

@app.get("/api/options/{state_name}")
async def get_options_by_state(state_name: str):
    if FRONTEND_OPTIONS_CACHE is None:
        raise HTTPException(status_code=503, detail="Options data is unavailable.")

    cleaned_state = state_name.lower().strip()
    if cleaned_state not in FRONTEND_OPTIONS_CACHE:
        raise HTTPException(status_code=404, detail=f"Data for state '{state_name}' not found. Please select from available states.")

    state_data = FRONTEND_OPTIONS_CACHE[cleaned_state]
    logging.info("Serving seasons and crops for state: %s", state_name)
    return {
        "state_name": state_name,
        "available_seasons": sorted(state_data.keys()),
        "season_crop_map": state_data,
    }

@app.post("/api/predict_yield")
async def predict_yield_endpoint(data: PredictInput):
    """
    Receives user inputs and returns the predicted yield (Tonnes/ha).
    Expected JSON shape (example):
    {
      "crop": "rice",
      "state_name": "maharashtra",
      "season": "kharif",
      "area": 0.5,
      "rainfall": 1200.5
    }
    """
    if not MODEL_LOADED:
        raise HTTPException(status_code=503, detail="ML Prediction service is unavailable. Check server logs for model load errors.")

    try:
        # Validate and coerce numeric inputs
        try:
            area = float(data.area)
        except Exception:
            raise HTTPException(status_code=422, detail="Invalid 'area' value; must be a number (hectares).")

        try:
            rainfall = float(data.rainfall)
        except Exception:
            raise HTTPException(status_code=422, detail="Invalid 'rainfall' value; must be a number (mm).")

        state = data.state_name.lower()
        season = data.season.lower()
        crop = data.crop.strip()

        logging.info("PREDICTING: Crop=%s, State=%s, Area=%.6f, Rainfall=%.2f", crop, state, area, rainfall)

        # Run prediction
        predicted_yield = run_prediction_logic(crop, state, season, area, rainfall)

        # Ensure predicted_yield is native Python float
        pred_native = to_json_friendly(predicted_yield)
        try:
            pred_float = float(pred_native)
        except Exception:
            logging.exception("Unexpected prediction shape/type: %r", pred_native)
            raise HTTPException(status_code=500, detail="Unexpected prediction output type from model.")

        total_production = pred_float * float(area)

        response = {
            "status": "success",
            "message": "Crop yield prediction calculated successfully.",
            "predicted_yield_per_ha": round(pred_float, 4),
            "unit": "Tonnes/Hectare",
            "predicted_total_production": round(float(total_production), 2),
            "area_ha": float(area),
        }

        return JSONResponse(content=response)

    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Invalid selection for prediction: {e}. Please ensure the combination of Crop, State, and Season is valid.")
    except HTTPException:
        # Re-raise to let FastAPI handle it
        raise
    except Exception as e:
        logging.exception("Prediction failed at execution: %s", e)
        raise HTTPException(status_code=500, detail="Prediction failed due to an internal error.")
