
# Industrial Data Monitoring
# Bronze Layer
# Author: Andressa Saldanha
#
# Public portfolio version using synthetic data.
# No confidential production records are included.

import pandas as pd

def load_production_data(file_path):
    """Load an Excel file into a Pandas DataFrame."""
    df = pd.read_excel(file_path, engine="openpyxl")

    # Remove completely empty rows
    df = df.dropna(how="all")

    return df



if __name__ == "__main__":
    from pathlib import Path

    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "production_sample.xlsx"

    df = load_production_data(file_path)

    print("Industrial Data Monitoring - Bronze Layer")
    print(f"Rows loaded: {len(df)}")
    print(f"Columns loaded: {len(df.columns)}")
    print(df.head())

