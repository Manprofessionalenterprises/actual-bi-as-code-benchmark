# 🏢 GROUPE ACTUAL — Pilotage Stratégique COMEX (Evidence.dev BI-as-Code)

Welcome to the **Evidence.dev** BI-as-Code Executive Report connected live to **Snowflake**.

```sql macro_metrics
select 
    sum(chiffre_affaires) as total_ca,
    sum(marge_brute) as total_marge,
    sum(heures_effectuees) as total_heures,
    count(distinct mission_id) as total_placements,
    round(sum(marge_brute) / sum(chiffre_affaires) * 100, 1) as tx_marge
from BENCHMARK_DB.ANALYTICS.FCT_PLACEMENTS
```

```sql agences_summary
select 
    nom_agence,
    agence_region,
    count(distinct mission_id) as total_placements,
    sum(chiffre_affaires) as total_ca,
    sum(marge_brute) as total_marge,
    sum(heures_effectuees) as total_heures
from BENCHMARK_DB.ANALYTICS.FCT_PLACEMENTS
group by 1, 2
order by total_ca desc
```

```sql secteurs_summary
select 
    client_secteur,
    sum(chiffre_affaires) as total_ca,
    sum(marge_brute) as total_marge
from BENCHMARK_DB.ANALYTICS.FCT_PLACEMENTS
group by 1
order by total_ca desc
```

<BigValue 
    data={macro_metrics} 
    value=total_ca 
    title="Chiffre d'Affaires Total (€)"
    fmt="eur"
/>

<BigValue 
    data={macro_metrics} 
    value=total_marge 
    title="Marge Brute Groupe (€)"
    fmt="eur"
/>

<BigValue 
    data={macro_metrics} 
    value=tx_marge 
    title="Taux de Marge Brute (%)"
    fmt="pct"
/>

<BigValue 
    data={macro_metrics} 
    value=total_placements 
    title="Placements Actifs"
/>

---

## 📈 Performance par Agence & Région (€)

<BarChart 
    data={agences_summary} 
    x=nom_agence 
    y=total_ca 
    title="Chiffre d'Affaires par Agence (€)"
    color=#3b82f6
/>

---

## 🍕 Répartition par Secteur Client

<BarChart 
    data={secteurs_summary} 
    x=client_secteur 
    y=total_ca 
    title="Chiffre d'Affaires par Secteur (€)"
    color=#10b981
    swapXY=true
/>

---

## 📑 Tableau d'Arbitrage Réseau (22 Agences)

<DataTable data={agences_summary} search=true pagination=true pageSize=10>
    <Column id=nom_agence title="Agence"/>
    <Column id=agence_region title="Région"/>
    <Column id=total_placements title="Placements"/>
    <Column id=total_heures title="Heures Travaillées"/>
    <Column id=total_ca title="Chiffre d'Affaires (€)" fmt="eur"/>
    <Column id=total_marge title="Marge Brute (€)" fmt="eur"/>
</DataTable>
