def load_data(df_cleaned):
"""Save the cleaned data to a CSV file."""
df_cleaned.to_csv("data/cleaned_flight_data.csv", index=False)
print(" Data Successfully Saved to 'cleaned_flight_data.csv'")
