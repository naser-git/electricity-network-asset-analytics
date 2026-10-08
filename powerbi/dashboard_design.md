# Power BI Dashboard Specification

## Page 1 — Network Overview
- Total sites
- Total transformer capacity
- Average utilisation
- Number of sites above investigation threshold
- Average asset age
- Capacity headroom
- Demand vs capacity by region

## Page 2 — Asset Performance
- Winter vs summer demand
- Utilisation distribution
- Capacity headroom
- Asset age distribution
- Top 10 high-utilisation sites

## Page 3 — Geospatial Analysis
- Map of network sites
- Bubble size: transformer capacity
- Tooltip: demand, capacity, utilisation and asset age
- Region and investigation-band slicers

## Suggested DAX

```DAX
Average Utilisation % =
AVERAGEX(
    network_sites,
    DIVIDE(network_sites[winter_demand], network_sites[transformer_capacity])
)

Capacity Headroom =
SUM(network_sites[transformer_capacity]) - SUM(network_sites[winter_demand])

Average Asset Age =
YEAR(TODAY()) - AVERAGE(network_sites[commission_year])
```

Thresholds used in the portfolio analysis are illustrative and must not be presented as network-operator engineering limits.
