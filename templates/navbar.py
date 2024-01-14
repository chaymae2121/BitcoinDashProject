import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("About us", href="/aboutus")),
        dbc.NavItem(dbc.NavLink("Representation", href="/representation")),
        dbc.NavItem(dbc.NavLink("Clustering", href="/clustering")),
        dbc.NavItem(dbc.NavLink("Network", href="/network")),
    ],
    color="primary",
    brand_href="/",
    dark=True,
    brand=html.Span([html.I(className="fa-brands fa-bitcoin mr-2"), "BitcoinDash"]), 
    className="navbar navbar-expand-lg bg-primary",
)
