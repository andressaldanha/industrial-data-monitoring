
# Industrial Data Monitoring
# Silver Layer
# Author: Andressa Saldanha
# Public portfolio - Synthetic data

import pandas as pd
from bronze import load_production_data
from pathlib import Path


def process_silver(df_bronze):
    """Apply industrial production business rules."""

    df = df_bronze.copy()

    # 1. Calculate excess operation time
    df["Tempo Excedente"] = (
        df["Tempo Operação"]
        - df["Tempo Operac Padrão"]
    ).clip(lower=0)


    # 2. Calculate downtime difference
    df["Diferença Parada"] = (
        df["Tempo Operação"]
        - df["Tempo Operac Padrão"]
        - df["Tempo Parada"]
    ).round(6)


    # 3. Classify efficiency
    def classify_efficiency(value):
        if pd.isna(value):
            return "SEM EFICIÊNCIA"

        if value < 0.90:
            return "ABAIXO DE 90%"

        if value > 1.00:
            return "ACIMA DE 100%"

        return "DENTRO DO PADRÃO"

    df["Status Eficiência"] = (
        df["Eficiência"].apply(classify_efficiency)
    )

    # 4. Identify potential missing downtime
    df["Possível Parada Não Apontada"] = (
        (df["Eficiência"] < 0.90)
        & (df["Diferença Parada"] > 0)
    )

    # 5. Print monitoring results
    print("\n=== SILVER LAYER ===")
    print(f"Total records: {len(df)}")

    print("\nEfficiency classification:")
    print(df["Status Eficiência"].value_counts())

    print("\nPotential missing downtime:")
    print(
        df.loc[
            df["Possível Parada Não Apontada"],
            [
                "Ordem Prod",
                "Centro Trabalho",
                "Eficiência",
                "Tempo Excedente",
                "Diferença Parada"
            ]
        ].to_string(index=False)
    )

    print("\nSilver processing completed!")

    return df


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root / "data" / "production_sample.xlsx"
    )

    df_bronze = load_production_data(file_path)

    df_silver = process_silver(df_bronze)
