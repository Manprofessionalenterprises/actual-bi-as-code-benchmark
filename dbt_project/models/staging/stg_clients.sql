select
    client_id,
    nom_entreprise,
    secteur as secteur_activite,
    ville
from {{ source('raw', 'raw_clients') }}
