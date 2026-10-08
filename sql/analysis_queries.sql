-- Expected table: network_sites
-- site_id, region, latitude, longitude, commission_year,
-- transformer_count, transformer_capacity, winter_demand, summer_demand

-- Calculate winter utilisation and headroom
SELECT site_id,
       region,
       winter_demand,
       transformer_capacity,
       (winter_demand / NULLIF(transformer_capacity, 0)) * 100 AS utilisation_percentage,
       transformer_capacity - winter_demand AS capacity_headroom
FROM network_sites
ORDER BY utilisation_percentage DESC;

-- Sites above an illustrative 80% investigation threshold
SELECT site_id, region, winter_demand, transformer_capacity,
       (winter_demand / NULLIF(transformer_capacity, 0)) * 100 AS utilisation_percentage
FROM network_sites
WHERE (winter_demand / NULLIF(transformer_capacity, 0)) * 100 > 80
ORDER BY utilisation_percentage DESC;

-- Average utilisation by region
SELECT region,
       AVG((winter_demand / NULLIF(transformer_capacity, 0)) * 100) AS avg_utilisation_pct
FROM network_sites
GROUP BY region
ORDER BY avg_utilisation_pct DESC;

-- Older assets with limited headroom
SELECT site_id, region, commission_year,
       transformer_capacity, winter_demand,
       transformer_capacity - winter_demand AS capacity_headroom
FROM network_sites
WHERE commission_year < 2000
  AND transformer_capacity - winter_demand < 20
ORDER BY capacity_headroom ASC;
