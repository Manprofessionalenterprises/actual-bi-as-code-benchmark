select
    agence_id,
    nom_agence,
    region,
    directeur,
    objectifs_ca_annuel
from {{ source('raw', 'raw_agences') }}
