import os
import subprocess

base_dir = "/tmp/actual_dbt_clean/lightdash/spaces/shared"
os.makedirs(base_dir, exist_ok=True)

# 1. Performance par Agence with eChartsConfig
chart1_yaml = """version: 1
contentType: chart
slug: performance-par-agence
name: "1. Performance par Agence (CA & Marge)"
spaceSlug: shared
tableName: fct_placements
metricQuery:
  exploreName: fct_placements
  dimensions:
    - fct_placements_nom_agence
  metrics:
    - fct_placements_total_chiffre_affaires
    - fct_placements_total_marge_brute
  tableCalculations: []
  filters: {}
  sorts:
    - fieldId: fct_placements_total_chiffre_affaires
      descending: true
  limit: 500
chartConfig:
  type: cartesian
  config:
    layout:
      xField: fct_placements_nom_agence
      yField:
        - fct_placements_total_chiffre_affaires
        - fct_placements_total_marge_brute
    eChartsConfig:
      series:
        - type: bar
          encode:
            xRef:
              fieldId: fct_placements_nom_agence
            yRef:
              fieldId: fct_placements_total_chiffre_affaires
        - type: bar
          encode:
            xRef:
              fieldId: fct_placements_nom_agence
            yRef:
              fieldId: fct_placements_total_marge_brute
"""

# 3. CA par Region with eChartsConfig
chart3_yaml = """version: 1
contentType: chart
slug: ca-par-region
name: "3. CA & Rentabilité par Région"
spaceSlug: shared
tableName: fct_placements
metricQuery:
  exploreName: fct_placements
  dimensions:
    - fct_placements_agence_region
  metrics:
    - fct_placements_total_chiffre_affaires
    - fct_placements_total_marge_brute
  tableCalculations: []
  filters: {}
  sorts:
    - fieldId: fct_placements_total_chiffre_affaires
      descending: true
  limit: 500
chartConfig:
  type: cartesian
  config:
    layout:
      xField: fct_placements_agence_region
      yField:
        - fct_placements_total_chiffre_affaires
        - fct_placements_total_marge_brute
    eChartsConfig:
      series:
        - type: bar
          encode:
            xRef:
              fieldId: fct_placements_agence_region
            yRef:
              fieldId: fct_placements_total_chiffre_affaires
        - type: bar
          encode:
            xRef:
              fieldId: fct_placements_agence_region
            yRef:
              fieldId: fct_placements_total_marge_brute
"""

with open(os.path.join(base_dir, "performance-par-agence.chart.yml"), "w") as f:
    f.write(chart1_yaml)

with open(os.path.join(base_dir, "ca-par-region.chart.yml"), "w") as f:
    f.write(chart3_yaml)

print("🎉 Fichiers YAML mis à jour avec eChartsConfig !")
