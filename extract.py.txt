import pandas as pd

def extract_data():
"""Extract flight and passenger data from CSV files."""
df_flights = pd.read_csv("data/flights.csv")
df_passengers = pd.read_csv("data/passengers.csv")
print("Data Extraction Complete.")
return df_flights, df_passengers
