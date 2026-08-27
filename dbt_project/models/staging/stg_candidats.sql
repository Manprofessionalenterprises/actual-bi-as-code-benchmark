select
    candidat_id,
    nom_prenom as candidat_nom_complet,
    metier_principal as candidat_metier,
    statut,
    experience_annees
from {{ source('raw', 'raw_candidats') }}
