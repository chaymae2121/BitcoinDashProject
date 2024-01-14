import dash_cytoscape as cyto
import dash_html_components as html
from dash import dcc, Input, Output, callback

from dataset.operations import fetch_dataset
import networkx as nx

# Load data from a local CSV file
df = fetch_dataset()

df_true = df[df["cluster_src"] != df["cluster_dst"]]
df_net = df_true.groupby(["V1_src_actor", "V1_dst_actor"]).agg({"value": ["sum", "count"]}).reset_index()
df_net_top = df_net.sort_values(("value", "count"), ascending=False)[:30]

# Create a network graph
G = nx.from_pandas_edgelist(df_net_top, source="V1_src_actor", target="V1_dst_actor")

# Create node and edge lists for Cytoscape
nodes = [{'data': {'id': str(node), 'label': str(node)}} for node in G.nodes]
edges = [{'data': {'source': str(edge[0]), 'target': str(edge[1])}} for edge in G.edges]

# Define the layout of the app
layout = html.Div([
    html.H1("Transactions network"),

    # Input for changing the number of transactions to display
    html.Label('Number of Transactions to Display:', className='form-label'),  # Added 'form-label' class
    dcc.Input(
        id='transactions-input',
        type='number',
        value=20,
        style={'marginBottom': 10},
        className='form-control'  # Added 'form-control' class
    ),

    cyto.Cytoscape(
        id='network-graph',
        elements=nodes + edges,
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '600px'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'content': 'data(label)',
                    'background-color': '#6FB1FC',
                    'border-width': 2,
                    'border-color': '#4B8B9B',
                    'color': '#000',
                    'font-size': '10px'
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'width': 2,
                    'line-color': '#ccc',
                    'target-arrow-color': '#ccc',
                    'target-arrow-shape': 'triangle'
                }
            }
        ]
    )
])

# Callback to update the graph based on the number of transactions input
@callback(
    Output('network-graph', 'elements'),
    [Input('transactions-input', 'value')]
)
def update_graph(num_transactions):
    # Filter the top transactions based on the input value
    df_net_top_updated = df_net.sort_values(("value", "count"), ascending=False)[:num_transactions]

    # Create a new network graph
    G_updated = nx.from_pandas_edgelist(df_net_top_updated, source="V1_src_actor", target="V1_dst_actor")

    # Create node and edge lists for Cytoscape
    nodes_updated = [{'data': {'id': str(node), 'label': str(node)}} for node in G_updated.nodes]
    edges_updated = [{'data': {'source': str(edge[0]), 'target': str(edge[1])}} for edge in G_updated.edges]

    return nodes_updated + edges_updated
