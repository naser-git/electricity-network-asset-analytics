from pathlib import Path
import pandas as pd

INPUT = Path("data/network_sites_clean.csv")
OUTPUT = Path("data/network_sites_analysed.csv")


def analyse(df: pd.DataFrame) -> pd.DataFrame:
    required = {"transformer_capacity", "winter_demand", "summer_demand"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    result = df.copy()
    result["winter_utilisation_pct"] = (
        result["winter_demand"] / result["transformer_capacity"] * 100
    )
    result["summer_utilisation_pct"] = (
        result["summer_demand"] / result["transformer_capacity"] * 100
    )
    result["winter_headroom"] = result["transformer_capacity"] - result["winter_demand"]
    result["summer_headroom"] = result["transformer_capacity"] - result["summer_demand"]

    # Illustrative portfolio-analysis band, not an operator limit.
    result["investigation_band"] = pd.cut(
        result["winter_utilisation_pct"],
        bins=[-float("inf"), 60, 80, 90, float("inf")],
        labels=["Low", "Moderate", "High", "Critical / investigate"],
    )
    return result


if __name__ == "__main__":
    if not INPUT.exists():
        raise FileNotFoundError(f"Run 01_load_clean.py first: {INPUT}")
    df = pd.read_csv(INPUT)
    result = analyse(df)
    result.to_csv(OUTPUT, index=False)
    print(result[["winter_utilisation_pct", "winter_headroom"]].describe())
    print("\nInvestigation bands:\n", result["investigation_band"].value_counts(dropna=False))
