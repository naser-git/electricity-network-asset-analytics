# Data

Raw third-party data is intentionally not committed to this repository.

## Source
UK Power Networks Open Data Portal:
https://ukpowernetworks.opendatasoft.com/explore/

Download the current Grid and Primary Sites dataset and save the compatible CSV locally as:

`data/grid_primary_sites.csv`

Then update `COLUMN_MAP` in `python/01_load_clean.py` to match the exact field names in the current export.

Run the scripts in order:

1. `python/01_load_clean.py`
2. `python/02_asset_utilisation_analysis.py`
3. `python/03_geospatial_analysis.py`

Check the dataset licence and redistribution terms before publishing any downloaded raw or cleaned data.
