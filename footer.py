# footer.py
from dash import html

project_url = "https://github.com/KangSolC/Dash-App"

footer_style = {
    'display': 'flex',
    'justify-content': 'center',
    'align-items': 'center',
    'background-color': '#0D6EFD',
    'color':'#FFF',
    'position': 'fixed',
    'bottom': '0',
    'width':'100%'
}

footer = html.Footer(
    children=([
        html.Div([
            html.I(className="fas fa-copyright"),
            html.Div("Copyright 2023"),
        ],
        style={'display': 'flex', 'align-items': 'center'}
    )]),
    style=footer_style)
