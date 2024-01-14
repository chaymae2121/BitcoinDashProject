import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Utiliser le thème Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Création du layout pour la page d'accueil (home)
layout = html.Div([
    # Titre en haut et au centre de la page
    html.H2("Bitcoin Transaction Network Dashboard", className='text-center mt-4', style={'color': '#6c757d'}),

    dbc.Row([
        # Partie gauche (image)
        dbc.Col(
            html.Img(src="/assets/bitcoin1.jpg", style={'width': '100%', 'height': 'auto'}),
            width=7,
            className='align-self-center text-center'
        ),

        # Partie droite (paragraphe et bouton)
        dbc.Col([
            html.P("Explore the intricate web of Bitcoin transactions with our interactive dashboard. This tool transforms raw blockchain data into a user-friendly format, where each line represents a payment from one entity to another. By replacing addresses with corresponding entities, the dashboard unveils a clear distinction between actual payments and technical change transactions within the Bitcoin ecosystem. Dive into the world of economic transactions, gaining valuable insights into financial flows and entity interactions. Our intuitive dashboard offers a streamlined experience for understanding the dynamics of Bitcoin transactions, providing a comprehensive overview of the network's financial activities.", style={'margin-top': '50px'}),  # Ajout de la marge supérieure
            dbc.Button("About us", id="button", n_clicks=0, color="primary", href="/aboutus", style={'margin-right': '10px'}),
            dbc.Button("Github link", id="button", n_clicks=0, color="primary", href="https://github.com/Yquetzal/Bitcoin-Datathon/blob/main/Entity_network_101.ipynb"),
        ], width=5, className='align-self-start text-left'),  # Changement ici pour aligner le texte à gauche
    ], className="justify-content-center mt-5"),

    # Redirection vers la page /aboutus
    dcc.Location(id='url_redirect'),
    html.Div(id='redirect')
], className="container", style={'margin': '10px'})

if __name__ == '__main__':
    app.run_server(debug=True)
