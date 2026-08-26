with agences as (
    select * from {{ ref('stg_agences') }}
),
missions as (
    select * from {{ ref('stg_missions') }}
)

select
    a.agence_id,
    a.nom_agence,
    a.ville,
    a.region,
    a.date_ouverture,
    count(distinct m.mission_id) as total_missions,
    coalesce(sum(m.heures_effectuees * m.taux_horaire_facture), 0) as chiffre_affaires_total
from agences a
left join missions m on a.agence_id = m.agence_id
group by 1, 2, 3, 4, 5
