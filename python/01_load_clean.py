"""Load and standardise a downloaded UKPN network-sites CSV.

Column names vary by export. Update COLUMN_MAP after downloading the current
open-data export so the analytical columns match the project schema.
"""

from pathlib import Path
import pandas as pd

INPUT = Path("data/grid_primary_sites.csv")
OUTPUT = Path("data/network_sites_clean.csv")

COLUMN_MAP = {
    # Replace source names with the current export names where necessary.
    "site_id": "site_id",
    "region": "region",
    "latitude": "latitude",
    "longitude": "longitude",
    "commission_year": "commission_year",
    "transformer_capacity": "transformer_capacity",
    "winter_demand": "winter_demand",
    "summer_demand": "summer_demand",
}


def clean(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {source: target for target, source in COLUMN_MAP.items() if source in df.columns}
    df = df.rename(columns=rename_map).copy()

    numeric = [
        "latitude", "longitude", "commission_year",
        "transformer_capacity", "winter_demand", "summer_demand",
    ]
    for column in numeric:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.drop_duplicates()
    if "site_id" in df.columns:
        df = df.dropna(subset=["site_id"])
    return df


if __name__ == "__main__":
    if not INPUT.exists():
        raise FileNotFoundError(f"Download the source CSV to {INPUT}")
    raw = pd.read_csv(INPUT)
    cleaned = clean(raw)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(OUTPUT, index=False)
    print(f"Saved {len(cleaned):,} rows to {OUTPUT}")
