import pandas as pd

def transform_data(df_flights, df_passengers):
"""Clean & transform flight data."""
df_flights["departure_time"] = pd.to_datetime(df_flights["departure_time"])
df_flights["arrival_time"] = pd.to_datetime(df_flights["arrival_time"])

# Fill missing delay values with 0
df_flights.fillna({"delay_minutes": 0}, inplace=True)

# Standardize airline names
df_flights["airline"] = df_flights["airline"].str.upper()

# Calculate flight duration (in minutes)
df_flights["flight_duration"] = (df_flights["arrival_time"] - df_flights["departure_time"]).dt.total_seconds() / 60

# Merge flight & passenger data
df_merged = df_flights.merge(df_passengers, on="flight_id", how="left")

print("✅ Data Transformation Complete.")
return df_merged
