# 📊 Dashboard BI-as-Code — Performance Placements & Agences

Welcome to the **Evidence.dev** BI-as-Code Benchmark report connected live to **Snowflake**.

```sql placements_summary
select 
    nom_agence,
    count(distinct mission_id) as total_placements,
    sum(chiffre_affaires) as total_ca,
    sum(marge_brute) as total_marge
from BENCHMARK_DB.ANALYTICS.FCT_PLACEMENTS
group by 1
order by total_ca desc
```

## 📈 Chiffre d'Affaires par Agence (€)

<BarChart 
    data={placements_summary} 
    x=nom_agence 
    y=total_ca 
    title="Chiffre d'Affaires (€)"
    color=#3b82f6
/>

---

## 📑 Détail des Performances Réseau

<DataTable data={placements_summary} search=true pagination=true>
    <Column id=nom_agence title="Agence"/>
    <Column id=total_placements title="Nombre de Placements"/>
    <Column id=total_ca title="Chiffre d'Affaires (€)" fmt="eur"/>
    <Column id=total_marge title="Marge Brute (€)" fmt="eur"/>
</DataTable>
