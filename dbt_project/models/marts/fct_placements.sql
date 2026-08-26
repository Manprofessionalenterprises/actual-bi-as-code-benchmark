with missions as (
    select * from {{ ref('stg_missions') }}
),
agences as (
    select * from {{ ref('stg_agences') }}
),
clients as (
    select * from {{ ref('stg_clients') }}
),
candidats as (
    select * from {{ ref('stg_candidats') }}
)

select
    m.mission_id,
    m.intitule_mission,
    m.statut,
    m.date_debut,
    m.date_fin,
    
    -- Foreign Keys & Details
    a.agence_id,
    a.nom_agence,
    a.region as agence_region,
    
    c.client_id,
    c.nom_entreprise as client_nom,
    c.secteur_activite as client_secteur,
    
    cand.candidat_id,
    concat(cand.prenom, ' ', cand.nom) as candidat_nom_complet,
    cand.metier as candidat_metier,
    
    -- Metrics Calculations
    m.heures_effectuees,
    m.taux_horaire_facture,
    m.taux_horaire_paye,
    
    (m.heures_effectuees * m.taux_horaire_facture) as chiffre_affaires,
    (m.heures_effectuees * m.taux_horaire_paye) as cout_paie,
    ((m.heures_effectuees * m.taux_horaire_facture) - (m.heures_effectuees * m.taux_horaire_paye)) as marge_brute

from missions m
left join agences a on m.agence_id = a.agence_id
left join clients c on m.client_id = c.client_id
left join candidats cand on m.candidat_id = cand.candidat_id
