import pandas as pd
import os
import requests

# URL de l'ensemble de données que vous souhaitez télécharger
url = "http://cazabetremy.fr/datasets/bitcoin2days/2days_entity_network.csv"

# Nom du fichier CSV local dans lequel vous souhaitez enregistrer l'ensemble de données
local_filename = "dataset/twodays_entity_network.csv"

# Créez le dossier 'dataset' s'il n'existe pas déjà
os.makedirs(os.path.dirname(local_filename), exist_ok=True)

# Téléchargez le fichier à partir de l'URL
response = requests.get(url)
with open(local_filename, 'wb') as file:
    file.write(response.content)