
from dash import html
from apps import commonmodule as cm
layout=html.Div([
    cm.top,
    html.Div([
        cm.navigationpanel,
        html.Div([
    html.H2("This is the Homepage")
],className="body")
    ],className='flex container')
])
