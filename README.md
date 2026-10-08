# Electricity Network Asset & Capacity Analytics

A portfolio project analysing electricity-network sites, transformer capacity, demand and geospatial information to identify potentially highly utilised assets and areas for further investigation.

## Objective
Connect electrical-engineering knowledge with data analytics by calculating asset utilisation, capacity headroom, asset age and regional patterns.

## Data source
UK Power Networks Open Data Portal:
https://ukpowernetworks.opendatasoft.com/explore/

The project is designed around the Grid and Primary Sites dataset. Raw third-party data is not committed to this repository.

## Core metric
**Utilisation % = Demand / Transformer Capacity × 100**

The project may use illustrative investigation bands such as <60%, 60–80%, 80–90% and >90%. These are portfolio-analysis thresholds, not SP Energy Networks operational limits.

## Workflow
Open data → Python cleaning → utilisation/headroom calculations → SQL analysis → geospatial analysis → Power BI dashboard

## KPIs
- Total network sites
- Total transformer capacity
- Average utilisation
- Highest utilisation
- Sites above investigation threshold
- Average asset age
- Winter vs summer demand
- Capacity headroom

## Dashboard pages
1. **Network Overview** – site count, capacity, demand, utilisation and regional comparison.
2. **Asset Performance** – transformer utilisation, headroom, asset age and high-utilisation sites.
3. **Geospatial Analysis** – site locations, demand, capacity and utilisation.

## Repository structure
```text
electricity-network-asset-analytics/
├── python/
│   ├── 01_load_clean.py
│   ├── 02_asset_utilisation_analysis.py
│   └── 03_geospatial_analysis.py
├── sql/
│   └── analysis_queries.sql
├── powerbi/
│   └── dashboard_design.md
├── data/
│   └── README.md
├── requirements.txt
└── README.md
```

## Disclaimer
This is a personal/academic portfolio project using public data. It does not represent operational analysis for SP Energy Networks or any other network operator. Results should be treated as analytical indicators for further investigation, not engineering decisions.
