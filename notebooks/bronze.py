
# Industrial Data Monitoring
# Bronze Layer
# Author: Andressa Saldanha
# Public portfolio - Synthetic data

from pathlib import Path
import pandas as pd

EXPECTED_COLUMNS = [
    "Estab",
    "Ordem Prod",
    "Centro Trabalho",
    "Item",
    "Descrição Item",
    "Qtd Reportada",
    "Início Reporte",
    "Hora Início Reporte",
    "Fim Reporte",
    "Hora Fim Reporte",
    "Tempo Operac Padrão",
    "Tempo Operação",
    "Tempo Parada",
    "Eficiência",
    "Nome Usuário",
]


def load_production_data(file_path):
    """Read and validate the synthetic production dataset."""

    # 1. Read Excel
    df = pd.read_excel(
        file_path,
        engine="openpyxl",
        dtype={"Item": str}
    )

    # 2. Remove completely empty rows
    df = df.dropna(how="all").copy()

    # 3. Normalize column names
    df.columns = df.columns.str.strip()

    # 4. Validate required columns
    missing = [
        col for col in EXPECTED_COLUMNS
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    # 5. Keep expected columns in original order
    df = df[EXPECTED_COLUMNS].copy()

    # 6. Convert identifiers
    df["Ordem Prod"] = pd.to_numeric(
        df["Ordem Prod"], errors="raise"
    ).astype("Int64")

    # Preserve existing leading zeros
    df["Item"] = df["Item"].astype("string").str.strip()

  
 
    # 7. Convert dates
    date_columns = [
        "Início Reporte",
        "Fim Reporte"
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(
            df[col],
            errors="raise",
            format="%Y-%m-%d"
        )

    # 8. Convert numeric columns
    numeric_columns = [
        "Qtd Reportada",
        "Tempo Operac Padrão",
        "Tempo Operação",
        "Tempo Parada",
        "Eficiência"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col], errors="raise"
        )

    # 9. Report results
    print("\n=== BRONZE LAYER ===")
    print(f"Rows loaded: {len(df)}")
    print(f"Columns loaded: {len(df.columns)}")

    print("\nData types:")
    print(df.dtypes)

    print("\nFirst 5 records:")
    print(df.head().to_string(index=False))

    print("\nBronze validation completed!")

    return df


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root / "data" / "production_sample.xlsx"
    )

    df_bronze = load_production_data(file_path)
