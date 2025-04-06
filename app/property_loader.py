import pandas as pd

def load_properties(file_path: str = "data/properties.csv"):
    df = pd.read_csv(file_path)
    required_cols = {"property", "latitude", "longitude"}
    if not required_cols.issubset(df.columns):
        raise ValueError("CSV must contain 'property', 'latitude', and 'longitude' columns.")
    return df.to_dict(orient="records")