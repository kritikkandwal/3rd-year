custom():
#     if os.path.exists("weather_data.json"):
#         with open("weather_data.json", "r+") as file:
#             data = json.load(file)
#             data["custom_city_info"] = {
#                 "local_name": "Kotdwar",
#                 "region": "Uttarakhand",
#                 "visited": False
#             }
#             file.seek(0)
#             json.dump(data, file, indent=4)
#         print("✅ PUT: Custom city info added/updated.\n")
#     else:
#         print("❌ PUT: File not found. Run GET first.")