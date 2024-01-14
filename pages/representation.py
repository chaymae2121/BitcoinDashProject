# aboutus.py
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash
from dataset.operations import fetch_dataset

# Créer des données fictives
data1 = {
    'Category': fetch_dataset()['type_src'].value_counts(dropna=False).reset_index(name='comptage')['type_src'].tolist(),
    'Values': fetch_dataset()['type_src'].value_counts(dropna=False).reset_index(name='comptage')['comptage'].tolist()
}
# data2 = {
#     'Category': fetch_dataset()['cluster_src'].value_counts(dropna=False).reset_index(name='comptage')['cluster_src'].tolist(),
#     'Values': fetch_dataset().groupby("cluster_src").agg({"valueUSD":"count"}).tolist()
# }


df1 = pd.DataFrame(data1)
df1 = pd.DataFrame(data1)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Définir la mise en page
layout = html.Div([
    dbc.Row(
        [
            dbc.Col([
                html.H3("Page avec un seul graphe et callback", style={'text-align': 'center'}),
                dcc.Graph(
        id='example-graph',
        figure=px.bar(df1, x='Category', y='Values', title='Graphe à Barres')
    )
            ], width=6),
            
            dbc.Col([
                html.H3("Graphe 2", style={'text-align': 'center'}),
                dcc.Graph(
                    figure={
                        # Ajoutez les données et la mise en page de votre deuxième graphe ici
                    }
                )
            ], width=6),
        ],
        className="mt-4 justify-content-center"
    ),

    dbc.Row(
        [
            dbc.Col([
                html.H3("Graphe 3", style={'text-align': 'center'}),
                dcc.Graph(
                    figure={
                        # Ajoutez les données et la mise en page de votre troisième graphe ici
                    }
                )
            ], width=6),

            dbc.Col([
                html.H3("Graphe 4", style={'text-align': 'center'}),
                dcc.Graph(
                    figure={
                        # Ajoutez les données et la mise en page de votre quatrième graphe ici
                    }
                )
            ], width=6),
        ],
        className="mt-4 justify-content-center"
    ),

    dbc.Row(
        [
            dbc.Col([
                html.H3("Graphe 5", style={'text-align': 'center'}),
                dcc.Graph(
                    figure={
                        # Ajoutez les données et la mise en page de votre cinquième graphe ici
                    }
                )
            ], width=6),

            dbc.Col([
                html.H3("Graphe 6", style={'text-align': 'center'}),
                dcc.Graph(
                    figure={
                        # Ajoutez les données et la mise en page de votre sixième graphe ici
                    }
                )
            ], width=6),
        ],
        className="mt-4 justify-content-center"
    ),

    html.Div([
        html.P("Bienvenue sur la page 'About Us'. Ici, vous pouvez en apprendre davantage sur notre équipe et notre projet."),
    ], style={'text-align': 'center', 'margin-top': '20px'}),
])

# Callback pour mettre à jour le titre du graphe en fonction de l'entrée utilisateur
@app.callback(
    Output('example-graph', 'figure'),
    [Input('graph-title-input', 'value')]
)
def update_graph(title):
    fig = px.bar(df1, x='Category', y='Values', title=title)
    return fig


# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)
