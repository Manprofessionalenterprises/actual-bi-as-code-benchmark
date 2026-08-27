select
    mission_id,
    agence_id,
    client_id,
    candidat_id,
    type_contrat,
    statut_mission as statut,
    date_debut,
    date_fin,
    heures_travaillees as heures_effectuees,
    taux_horaire_paye,
    taux_horaire_facture,
    chiffre_affaires,
    cout_salarial as cout_paie,
    marge_brute
from {{ source('raw', 'raw_missions') }}
