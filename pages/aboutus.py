import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Row(
        [
            dbc.Col([
                html.Img(src="/assets/chaymae.jpg", className="img-fluid mx-auto", style={'width': '250px', 'height': '250px'}),
                html.H3("Chaymae Mhajar", style={'text-align': 'center', 'font-size': '100%', 'margin-top': '10px'})
            ], width=3),

            dbc.Col([
                html.Img(src="/assets/benziza.jpg", className="img-fluid mx-auto", style={'width': '250px', 'height': '250px'}),
                html.H3("Mohamed Benziza", style={'text-align': 'center', 'font-size': '100%', 'margin-top': '10px'})
            ], width=3),
        ],
        className="mt-4 justify-content-center"
    ),

    html.Div([
        html.P("We are master's students in Information Technology and Web at Claude Bernard Lyon 1 University. This project is undertaken as part of a data analysis initiative, where we explore and visualize a simplified and enriched view of the Bitcoin blockchain data. In the original Bitcoin Blockchain dataset, transactions occur between anonymous addresses. Notably, multiple addresses can belong to the same Entity (Actor), be it a person, company, or other entities. Furthermore, a single transaction can encompass multiple payments directed towards various addresses and entities. Our goal is to analyze and represent this intricate web of Bitcoin transactions through an interactive dashboard, shedding light on the relationships between entities and providing a comprehensive overview of the financial activities within the Bitcoin network."),
    ], style={'text-align': 'center', 'margin': '0 auto', 'max-width': '800px', 'margin-top': '20px'}),
])
