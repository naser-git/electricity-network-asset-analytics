from pathlib import Path
import pandas as pd

INPUT = Path("data/network_sites_analysed.csv")


def validate_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    required = {"latitude", "longitude"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    result = df.copy()
    result = result.dropna(subset=["latitude", "longitude"])
    result = result[result["latitude"].between(-90, 90)]
    result = result[result["longitude"].between(-180, 180)]
    return result


if __name__ == "__main__":
    if not INPUT.exists():
        raise FileNotFoundError(f"Run 02_asset_utilisation_analysis.py first: {INPUT}")
    df = pd.read_csv(INPUT)
    geo = validate_coordinates(df)
    print("Valid mapped sites:", len(geo))
    print("\nTop mapped high-utilisation sites:")
    cols = [c for c in ["site_id", "region", "latitude", "longitude", "winter_utilisation_pct"] if c in geo.columns]
    print(geo.sort_values("winter_utilisation_pct", ascending=False)[cols].head(10))
