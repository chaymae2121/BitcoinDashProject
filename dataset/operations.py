# dataset/operations.py
import os
import pandas as pd

def fetch_dataset():
    # Obtenez le chemin complet du répertoire actuel
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Concaténez le chemin du fichier avec le répertoire actuel
    file_path = os.path.join(current_directory, 'twodays_entity_network_v.csv')

    # Charger le fichier CSV
    df = pd.read_csv(file_path)

    df['type_src'] = df['type_src'].fillna("None")

    return df