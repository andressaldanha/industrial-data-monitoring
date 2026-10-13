
# Industrial Data Monitoring
# Automated Tests - Silver Layer
# Author: Andressa Saldanha

import sys
from pathlib import Path

import pandas as pd
import pytest

# Import Silver module
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "notebooks"))

from silver import process_silver


def test_silver_calculations():

    # Synthetic production records
    df = pd.DataFrame({
        "Ordem Prod": [100001, 100002, 100003],
        "Centro Trabalho": ["LINHA_A", "LINHA_B", "LINHA_C"],
        "Tempo Operac Padrão": [0.50, 0.30, 0.40],
        "Tempo Operação": [0.50, 0.60, 0.35],
        "Tempo Parada": [0.00, 0.00, 0.00],
        "Eficiência": [1.00, 0.50, 0.40 / 0.35]
    })

    result = process_silver(df)

    # Efficiency classification
    assert result["Status Eficiência"].tolist() == [
        "DENTRO DO PADRÃO",
        "ABAIXO DE 90%",
        "ACIMA DE 100%"
    ]

    # Excess operation time
    assert result["Tempo Excedente"].round(2).tolist() == [
        0.00, 0.30, 0.00
    ]

    # Potential missing downtime
    assert result["Possível Parada Não Apontada"].tolist() == [
        False, True, False
    ]


def test_floating_point_precision():

    df = pd.DataFrame({
        "Ordem Prod": [100004],
        "Centro Trabalho": ["LINHA_A"],
        "Tempo Operac Padrão": [0.25],
        "Tempo Operação": [0.40],
        "Tempo Parada": [0.15],
        "Eficiência": [0.625]
    })

    result = process_silver(df)

    assert result["Diferença Parada"].iloc[0] == 0
    assert not result["Possível Parada Não Apontada"].iloc[0]

def test_efficiency_boundaries():

    df = pd.DataFrame({
        "Ordem Prod": [200001, 200002, 200003, 200004],
        "Centro Trabalho": ["A", "B", "C", "D"],
        "Tempo Operac Padrão": [0.9, 1.0, 0.89, 1.01],
        "Tempo Operação": [1.0, 1.0, 1.0, 1.0],
        "Tempo Parada": [0.0, 0.0, 0.0, 0.0],
        "Eficiência": [0.90, 1.00, 0.89, 1.01]
    })

    result = process_silver(df)

    assert result["Status Eficiência"].tolist() == [
        "DENTRO DO PADRÃO",
        "DENTRO DO PADRÃO",
        "ABAIXO DE 90%",
        "ACIMA DE 100%"
    ]


def test_downtime_fully_reported():

    df = pd.DataFrame({
        "Ordem Prod": [200005],
        "Centro Trabalho": ["LINHA_A"],
        "Tempo Operac Padrão": [0.25],
        "Tempo Operação": [0.40],
        "Tempo Parada": [0.15],
        "Eficiência": [0.625]
    })

    result = process_silver(df)

    
    assert result["Tempo Excedente"].iloc[0] == pytest.approx(0.15)
    assert result["Diferença Parada"].iloc[0] == 0
    assert not result["Possível Parada Não Apontada"].iloc[0]


def test_missing_efficiency():

    df = pd.DataFrame({
        "Ordem Prod": [200006],
        "Centro Trabalho": ["LINHA_B"],
        "Tempo Operac Padrão": [0.5],
        "Tempo Operação": [0.5],
        "Tempo Parada": [0.0],
        "Eficiência": [float("nan")]
    })

    result = process_silver(df)

    assert result["Status Eficiência"].iloc[0] == (
        "SEM EFICIÊNCIA"
    )
    assert not result["Possível Parada Não Apontada"].iloc[0]
