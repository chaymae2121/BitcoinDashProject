import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.cluster import DBSCAN
from dataset.operations import fetch_dataset_10000,prepare_data_for_clustering
from dash import html, dcc,callback

df = fetch_dataset_10000()

# Apply K-Means clustering
num_clusters_kmeans = 3
kmeans = KMeans(n_clusters=num_clusters_kmeans, random_state=42)
df['cluster_kmeans'] = kmeans.fit_predict(prepare_data_for_clustering())

# Apply Gaussian Mixtures clustering
num_clusters_gaussian = 3
gmm = GaussianMixture(n_components=num_clusters_gaussian, random_state=42)
df['cluster_gaussian'] = gmm.fit_predict(prepare_data_for_clustering())

# Apply DBScan clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
df['cluster_dbscan'] = dbscan.fit_predict(prepare_data_for_clustering())


# Mise en page de l'application
layout = html.Div([
    # Input pour changer la valeur de K dans K-Means
    html.Label('Choose the value of K for K-Means:',className='form-label'),
    dcc.Input(
        id='kmeans-input',
        type='number',
        value=num_clusters_kmeans,
        style={'marginBottom': 10},
        className='form-control'
    ),

    # Graphique pour afficher les clusters K-Means
    dcc.Graph(
        id='cluster-graph-kmeans',
        figure=px.scatter(df, x='valueUSD', y='nb_inputs', color='cluster_kmeans',
                          title=f'K-Means Clustering (k={num_clusters_kmeans})')
    ),

    # Input pour changer le nombre de composants pour Gaussian Mixtures
    html.Label('Choose the number of components for Gaussian Mixtures:',className='form-label'),
    dcc.Input(
        id='gaussian-input',
        type='number',
        value=num_clusters_gaussian,
        style={'marginBottom': 10},
        className='form-control'
    ),

    # Graphique pour afficher les clusters Gaussian Mixtures
    dcc.Graph(
        id='cluster-graph-gaussian',
        figure=px.scatter(df, x='valueUSD', y='nb_inputs', color='cluster_gaussian',
                          title=f'Gaussian Mixtures Clustering (k={num_clusters_gaussian})')
    ),

    # Input pour changer les paramètres d'epsilon et de min_samples pour DBScan
    html.Label('Choose epsilon for DBScan:',className='form-label'),
    dcc.Input(
        id='dbscan-epsilon-input',
        type='number',
        value=0.5,
        style={'marginBottom': 10},
        className='form-control'
    ),
    html.Label('Choose min_samples for DBScan:',className='form-label'),
    dcc.Input(
        id='dbscan-min-samples-input',
        type='number',
        value=5,
        style={'marginBottom': 10},
        className='form-control'
    ),

    # Graphique pour afficher les clusters DBScan
    dcc.Graph(
        id='cluster-graph-dbscan',
        figure=px.scatter(df, x='valueUSD', y='nb_inputs', color='cluster_dbscan',
                          title='DBScan Clustering')
    ),
])

# Callback pour mettre à jour le graphique K-Means en fonction de la valeur de K
@callback(
    dash.dependencies.Output('cluster-graph-kmeans', 'figure'),
    [dash.dependencies.Input('kmeans-input', 'value')]
)
def update_kmeans_graph(k_value):
    # Appliquer le clustering K-Means avec la nouvelle valeur de K
    kmeans = KMeans(n_clusters=int(k_value), random_state=42)
    df['cluster_kmeans'] = kmeans.fit_predict(prepare_data_for_clustering())

    # Créer le graphique K-Means mis à jour
    fig_kmeans = px.scatter(df, x='valueUSD', y='nb_inputs', color='cluster_kmeans',
                            title=f'K-Means Clustering (k={k_value})')

    return fig_kmeans

# Callback pour mettre à jour le graphique Gaussian Mixtures en fonction du nombre de composants
@callback(
    dash.dependencies.Output('cluster-graph-gaussian', 'figure'),
    [dash.dependencies.Input('gaussian-input', 'value')]
)
def update_gaussian_graph(gaussian_value):
    # Appliquer le clustering Gaussian Mixtures avec le nouveau nombre de composants
    gmm = GaussianMixture(n_components=int(gaussian_value), random_state=42)
    df['cluster_gaussian'] = gmm.fit_predict(prepare_data_for_clustering())

    # Créer le graphique Gaussian Mixtures mis à jour
    fig_gaussian = px.scatter(df, x='valueUSD', y='nb_inputs', color='cluster_gaussian',
                              title=f'Gaussian Mixtures Clustering (k={gaussian_value})')

    return fig_gaussian

# Callback pour mettre à jour le graphique DBScan en fonction des paramètres epsilon et min_samples
@callback(
    dash.dependencies.Output('cluster-graph-dbscan', 'figure'),
    [dash.dependencies.Input('dbscan-epsilon-input', 'value'),
     dash.dependencies.Input('dbscan-min-samples-input', 'value')]
)
def update_dbscan_graph(epsilon_value, min_samples_value):
    # Appliquer le clustering DBScan avec les nouveaux paramètres
    dbscan = DBSCAN(eps=float(epsilon_value), min_samples=int(min_samples_value))
    df['cluster_dbscan'] = dbscan.fit_predict(prepare_data_for_clustering())

    # Créer le graphique DBScan mis à jour
    fig_dbscan = px.scatter(df, x='valueUSD', y='nb_inputs', color='cluster_dbscan',
                            title='DBScan Clustering')

    return fig_dbscan
