import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


layout = html.Div([
    html.H2("Bitcoin Transaction Network Dashboard", className='text-center mt-4', style={'color': '#6c757d'}),

    dbc.Row([
        dbc.Col(
            html.Img(src="/assets/bitcoin.jpg", style={'width': '100%', 'height': 'auto'}),
            width=7,
            className='align-self-center text-center'
        ),

        dbc.Col([
            html.P("Explore the intricate web of Bitcoin transactions with our interactive dashboard. This tool transforms raw blockchain data into a user-friendly format, where each line represents a payment from one entity to another. By replacing addresses with corresponding entities, the dashboard unveils a clear distinction between actual payments and technical change transactions within the Bitcoin ecosystem. Dive into the world of economic transactions, gaining valuable insights into financial flows and entity interactions. Our intuitive dashboard offers a streamlined experience for understanding the dynamics of Bitcoin transactions, providing a comprehensive overview of the network's financial activities.", style={'margin-top': '50px'}), 
            dbc.Button("About us", id="button", n_clicks=0, color="primary", href="/aboutus", style={'margin-right': '10px'}),
            dbc.Button("Github link", id="button", n_clicks=0, color="primary", href="https://github.com/chaymae2121/BitcoinDashProject"),
        ], width=5, className='align-self-start text-left'),
    ], className="justify-content-center mt-5"),

    dcc.Location(id='url_redirect'),
    html.Div(id='redirect')
], className="container", style={'margin': '10px'})