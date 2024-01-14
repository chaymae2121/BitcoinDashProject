import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_dataset(file_path, nrows=None):
    # Get the full path of the current directory
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Concatenate the file path with the current directory
    full_file_path = os.path.join(current_directory, file_path)

    # Load CSV file
    df = pd.read_csv(full_file_path, nrows=nrows)

    # Convert 'timestamp' column to date format
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    return df

def fetch_dataset():
    return load_dataset('twodays_entity_network.csv')

def fetch_dataset_10000():
    return load_dataset('twodays_entity_network.csv', nrows=10000)

def dataset_day_diagram():
    df = load_dataset('twodays_entity_network.csv')

    # Add an 'hour' column to extract the time from each timestamp
    if 'timestamp' in df.columns:
        df['hour'] = df['timestamp'].dt.hour

    return df

def generate_category_data():
    data = {
        'Category': fetch_dataset()['type_src'].value_counts(dropna=False).reset_index(name='comptage')['type_src'].tolist(),
        'Values': fetch_dataset()['type_src'].value_counts(dropna=False).reset_index(name='comptage')['comptage'].tolist()
    }
    df = pd.DataFrame(data)
    return df

def calculate_totals_and_top_entities(df):
    # Obtenez toutes les entités uniques de 'V1_src_actor' et 'V1_dst_actor'
    entites_src = df['V1_src_actor'].unique()
    entites_dst = df['V1_dst_actor'].unique()
    entites_uniques = list(map(str, set(entites_src) | set(entites_dst)))

    # Initialiser des listes pour stocker les totaux des paiements envoyés et reçus
    totals_envoyes = []
    totals_recus = []

    # Calculer les totaux pour chaque entité (paiements envoyés)
    for entite in entites_uniques:
        paiements_envoyes = df[df['V1_src_actor'] == entite]['valueUSD'].sum()
        totals_envoyes.append((entite, paiements_envoyes))

    # Calculer les totaux pour chaque entité (paiements reçus)
    for entite in entites_uniques:
        paiements_recus = df[df['V1_dst_actor'] == entite]['valueUSD'].sum()
        totals_recus.append((entite, paiements_recus))

    # Trier les entités en fonction des totaux et sélectionner les 10 premières
    totals_envoyes.sort(key=lambda x: x[1], reverse=True)
    totals_recus.sort(key=lambda x: x[1], reverse=True)

    top_entites_envoyes = [entite[0] for entite in totals_envoyes[:10]]
    top_entites_recus = [entite[0] for entite in totals_recus[:10]]

    return top_entites_envoyes, top_entites_recus

def generate_df_top_envoyes(df, top_entites_envoyes):
    # Filtrer le DataFrame original pour inclure uniquement les 10 entités les plus importantes (paiements envoyés)
    df_top_envoyes = df[df['V1_src_actor'].isin(top_entites_envoyes)]
    return df_top_envoyes

def generate_df_top_recus(df, top_entites_recus):
    # Filtrer le DataFrame original pour inclure uniquement les 10 entités les plus importantes (paiements reçus)
    df_top_recus = df[df['V1_dst_actor'].isin(top_entites_recus)]
    return df_top_recus

def prepare_data_for_clustering():
    # Charger le dataset
    df = fetch_dataset_10000()

    # Sélectionner les colonnes pour le clustering
    selected_columns = ['valueUSD', 'nb_inputs']

    # Filtrer le DataFrame avec les colonnes sélectionnées
    data_for_clustering = df[selected_columns]

    # Gérer les valeurs manquantes si nécessaire
    data_for_clustering.fillna(0, inplace=True)  # Remplacer NaN par 0 pour la simplicité

    # Mise à l'échelle des fonctionnalités
    scaler = StandardScaler()
    data_for_clustering_scaled = scaler.fit_transform(data_for_clustering)

    return data_for_clustering_scaled