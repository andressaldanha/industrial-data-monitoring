
# Industrial Data Monitoring
# Data Visualization
# Author: Andressa Saldanha

from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT / "notebooks")
)

from bronze import load_production_data
from silver import process_silver


def generate_efficiency_chart():

    # Load synthetic data
    file_path = (
        PROJECT_ROOT / "data" / "production_sample.xlsx"
    )

    df_bronze = load_production_data(file_path)
    df_silver = process_silver(df_bronze)

    # Count efficiency categories
    categories = [
        "ABAIXO DE 90%",
        "DENTRO DO PADRÃO",
        "ACIMA DE 100%"
    ]

    counts = (
        df_silver["Status Eficiência"]
        .value_counts()
        .reindex(categories, fill_value=0)
    )

    labels = [
        "Below 90%",
        "90% - 100%",
        "Above 100%"
    ]

    # Dark Tech theme
    background = "#0D0B16"
    purple = "#A855F7"
    light_purple = "#C4B5FD"
    dark_purple = "#6D28D9"

    fig, ax = plt.subplots(figsize=(10, 5))

    fig.patch.set_facecolor(background)
    ax.set_facecolor(background)

    bars = ax.bar(
        labels,
        counts.values,
        color=[purple, light_purple, dark_purple],
        width=0.55
    )

    ax.set_title(
        "Industrial Efficiency Monitoring",
        color="white",
        fontsize=18,
        fontweight="bold",
        pad=25
    )

    ax.set_ylabel(
        "Production Records",
        color="white",
        fontsize=11
    )

    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")

    ax.set_ylim(
        0,
        max(counts.max() * 1.25, 1)
    )

    ax.yaxis.grid(
        True,
        color="#403451",
        alpha=0.35
    )

    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.12,
            str(int(bar.get_height())),
            ha="center",
            color="white",
            fontsize=14,
            fontweight="bold"
        )

    fig.text(
        0.5,
        0.02,
        "Synthetic Dataset | Python + Databricks Portfolio",
        ha="center",
        color="#B8A9D1",
        fontsize=9
    )

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    # Save chart
    output_dir = PROJECT_ROOT / "assets"
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "efficiency_chart.png"

    plt.savefig(
        output_path,
        dpi=180,
        facecolor=fig.get_facecolor()
    )

    plt.close(fig)

    print(f"\nChart created: {output_path}")


if __name__ == "__main__":
    generate_efficiency_chart()
