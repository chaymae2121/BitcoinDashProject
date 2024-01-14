import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dataset.operations import fetch_dataset,dataset_day_diagram,generate_category_data,calculate_totals_and_top_entities,generate_df_top_envoyes,generate_df_top_recus
from dash import html, dcc, Input, Output,callback


##START : Transactions par heure
transactions_par_jour_heure = dataset_day_diagram().groupby(['day', 'hour']).size().unstack()

jours_options = [{'label': str(jour), 'value': jour} for jour in dataset_day_diagram()['day'].unique()]
##END : Transactions par heure

##START : GRAPH 3
df2 = fetch_dataset()
top_entites_envoyes, top_entites_recus = calculate_totals_and_top_entities(df2)

df_top_envoyes = generate_df_top_envoyes(df2, top_entites_envoyes)
df_top_recus = generate_df_top_recus(df2, top_entites_recus)
##END : GRAPH 3


# Set layout
layout = html.Div([
    dbc.Row(
        [
            dbc.Col([
                html.H3("Total payments made by entity type", style={'text-align': 'center'}),
                dcc.Graph(
                    id='example-graph',
                    figure=px.bar(generate_category_data(), x='Category', y='Values',range_y=[0, 30000])
                )
            ], width=6),
            dbc.Col([
                html.H3("Number of transactions per hour"),

                # Input pour la couleur
                html.Label("Sélectionnez un jour :"),
                dcc.Dropdown(
                    id='dropdown-jour',
                    options=jours_options,
                    value=dataset_day_diagram()['day'].min(), 
                    multi=False
                ),
                dcc.Graph(
                    id='graph-transactions'
                )
            ], width=6),
        ],
        className="mt-4 justify-content-center"
    ),

    dbc.Row(
        [
            dbc.Col([
                html.H3(children='Total payments sent by entity'),
                dcc.Graph(
                    id='bar-envoyes',
                    figure=px.bar(df_top_envoyes, x='V1_src_actor', y='valueUSD', color='V1_src_actor', hover_data=[])
                )
            ], width=6),

            dbc.Col([
                html.H3(children='Total payments received by entity'),
                dcc.Graph(
                    id='bar-recus',
                    figure=px.bar(df_top_recus, x='V1_dst_actor', y='valueUSD', color='V1_dst_actor', hover_data=[])
                )
            ], width=6),
        ],
        className="mt-4 justify-content-center"
    ),
])


# Callback to update the graph based on the dropdown selection
@callback(
    Output('graph-transactions', 'figure'),
    [Input('dropdown-jour', 'value')]
)
def update_graph(selected_day):
    transactions_jour_selected = transactions_par_jour_heure.loc[selected_day]

    colorscale = px.colors.sequential.Viridis

    normalized_values = (transactions_jour_selected.values - transactions_jour_selected.min()) / (transactions_jour_selected.max() - transactions_jour_selected.min())

    figure = {
        'data': [
            {
                'x': transactions_jour_selected.index,
                'y': transactions_jour_selected.values,
                'type': 'bar',
                'name': 'Transactions',
                'marker': {'color': normalized_values, 'colorscale': colorscale}
            },
        ],
        'layout': {
            'title': f'Nombre de transactions par heure - Le {selected_day}/07/2016',
            'xaxis': {'title': 'Heure'},
            'yaxis': {'title': 'Nombre de transactions'},
        }
    }

    return figure