from dash import html

footer = html.Footer(
    children=[
        html.Div([
            html.I(className="fas fa-copyright"),
            html.Div("Copyright 2023"),
        ],
        className='d-flex align-items-center justify-content-center'),  
    ],
    className='fixed-bottom bg-primary text-white',
)
