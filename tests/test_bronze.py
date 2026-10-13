
# Industrial Data Monitoring
# Automated Tests - Bronze Layer
# Author: Andressa Saldanha

import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT / "notebooks")
)

from bronze import load_production_data, EXPECTED_COLUMNS


def test_bronze_loads_sample_data():
    """Check the synthetic Excel ingestion."""

    file_path = (
        PROJECT_ROOT / "data" / "production_sample.xlsx"
    )

    df = load_production_data(file_path)

    assert len(df) == 12
    assert len(df.columns) == 15
    assert df.columns.tolist() == EXPECTED_COLUMNS


def test_item_leading_zeros():
    """Check item identifiers preserve leading zeros."""

    file_path = (
        PROJECT_ROOT / "data" / "production_sample.xlsx"
    )

    df = load_production_data(file_path)

    assert df["Item"].iloc[0] == "000101"


def test_date_conversion():
    """Check report dates are converted."""

    file_path = (
        PROJECT_ROOT / "data" / "production_sample.xlsx"
    )

    df = load_production_data(file_path)

    assert pd.api.types.is_datetime64_any_dtype(
        df["Início Reporte"]
    )

    assert pd.api.types.is_datetime64_any_dtype(
        df["Fim Reporte"]
    )


def test_missing_required_column(tmp_path):
    """Check invalid Excel structure is rejected."""

    df = pd.DataFrame({
        "Ordem Prod": [100001],
        "Item": ["000101"]
    })

    file_path = tmp_path / "invalid_sample.xlsx"

    df.to_excel(file_path, index=False)

    with pytest.raises(
        ValueError,
        match="Missing required columns"
    ):
        load_production_data(file_path)
