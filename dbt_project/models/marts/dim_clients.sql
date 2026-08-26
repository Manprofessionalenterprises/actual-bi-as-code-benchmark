with clients as (
    select * from {{ ref('stg_clients') }}
),
missions as (
    select * from {{ ref('stg_missions') }}
)

select
    c.client_id,
    c.nom_entreprise,
    c.secteur_activite,
    c.ville,
    c.date_creation,
    count(distinct m.mission_id) as total_missions_commandees,
    coalesce(sum(m.heures_effectuees * m.taux_horaire_facture), 0) as total_facture
from clients c
left join missions m on c.client_id = m.client_id
group by 1, 2, 3, 4, 5
