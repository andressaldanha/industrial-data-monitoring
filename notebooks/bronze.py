
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
    print("Industrial Data Monitoring - Bronze Layer")
    print("Initial data ingestion module ready.")
