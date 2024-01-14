from dash import Dash, html, dcc, Input, Output
import dash
import dash_bootstrap_components as dbc
from pages import home,aboutus,representation,clustering,network
from dash_bootstrap_templates import load_figure_template
load_figure_template(["minty", "minty_dark"])
from templates.navbar import navbar
from templates.footer import footer


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME], suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        navbar,
        dbc.Container(id="page-content", fluid=True, style={'margin': '20px 0'}),
        dash.page_container,
        footer,
    ]
)

@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return home.layout
    if pathname == "/aboutus":
        return aboutus.layout
    elif pathname == "/representation":
        return representation.layout
    elif pathname == "/clustering":
        return clustering.layout
    elif pathname == "/network":
        return network.layout
    else:
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognized..."),
            ]
        )

if __name__ == '__main__':
    app.run(debug=False)
