import pandas as pd
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

OUTPUT_FILE = 'State_data.json'
INPUT_FILE = 'model/yeild_data.csv'

def generate_frontend_json_options(df_input):
    """
    Groups the unique State, Season, and Crop combinations
    into a hierarchical dictionary structure for frontend filtering:
    State -> Season -> [Crops]
    """
    logging.info("Starting JSON generation...")

    # 1. Select and prepare the necessary categorical columns
    df_options = df_input[['State_Name', 'Season', 'Crop']].copy()

    # Ensure categorical columns are clean (lowercase and stripped)
    for col in ['State_Name', 'Season', 'Crop']:
        df_options[col] = df_options[col].str.lower().str.strip()

    # 2. Group by State and Season, then aggregate unique crops into a list
    # .apply(lambda x: sorted(list(x.unique()))) ensures sorted lists of unique crops
    grouped_data = (
        df_options
        .groupby(['State_Name', 'Season'])['Crop']
        .apply(lambda x: sorted(list(x.unique())))
        .reset_index()
    )

    # 3. Create the final hierarchical dictionary structure
    options_dict = {}
    for state in sorted(grouped_data['State_Name'].unique()):
        state_data = grouped_data[grouped_data['State_Name'] == state]
        season_dict = {}

        for _, row in state_data.iterrows():
            season = row['Season']
            crops = row['Crop']
            season_dict[season] = crops

        # Sort seasons alphabetically for better frontend display
        options_dict[state] = dict(sorted(season_dict.items()))

    return options_dict

def save_json_file(json_data, filename):
    """Saves the Python dictionary to a formatted JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(json_data, f, indent=4)
        logging.info(f"Successfully saved options to {filename}")
    except Exception as e:
        logging.error(f"Failed to save JSON file: {e}")

if __name__ == '__main__':
    try:
        # Load your master cleaned data frame
        df = pd.read_csv(INPUT_FILE)

        # Generate the hierarchical structure
        options_data = generate_frontend_json_options(df)

        # Save the result to a file
        save_json_file(options_data, OUTPUT_FILE)

    except FileNotFoundError:
        logging.error(f"Error: Input file '{INPUT_FILE}' not found. Please ensure your cleaned dataset is present.")
    except Exception as e:
        logging.error(f"An unexpected error occurred during processing: {e}")