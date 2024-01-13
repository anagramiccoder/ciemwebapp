import plotly.graph_objs as go
from dash import html,dash_table,dcc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px
from app import app
from apps import dbconnect as db
navigationpanel = html.Nav([
    html.Div([
        html.H4("Main"),
        html.A("Home", href="/home",),
        html.A("Logout", href="#",id='lo',n_clicks=0),
    ],className="module-div"),
    html.Div([
        html.H4("Profile"),
        html.A("Edit Profile", href="/edit-profile",),
        html.A("Change Password", href="/change-password",),
    ],className="module-div"),
    html.Div([
        html.H4("Reaffilation"),
        html.A("Reaffilation Form",href="/reaffiliate"),
    ],className="module-div"),
    html.Div([
        html.H4("Members"),
        html.A("All Members", href="/members",),
    ],className="module-div"),
    html.Div([
        html.H4("Alumni"),
        html.A("All Alumni", href="/alumni",),
    ],className="module-div"),
    html.Div([
        html.H4("Account Management"),
        html.A("Update Member Status", href="/update-member",),
        html.A("Update Alumni Status", href="/update-alumni",),
        html.A("Managers", href="/managers?mode=view",),
    ],className="module-div"),
    html.Div([
        html.H4("Generation"),
        html.A("Generate Report", href="#",className="disabled-a"),
    ],className="module-div"),
],className="nav")

sectionbody=html.Div([
    html.H2("Report Generations"),
    html.H3("Tracking"),
    dcc.Graph(id='by-batch'),
    dcc.Graph(id='by-year'),
    dcc.Graph(id='by-committee'),
],className="body")
layout=html.Div([
        html.Div([html.A([html.Div([html.Img(src="./assets/logo.png",className="logo"),html.H2("UP CEIM")],className="flex center")],href="/home")],className="topbar"),
        html.Div([
            navigationpanel, 
            sectionbody,
            ],
            className='flex container'),])
@app.callback(
    [
        Output('by-batch','figure'),
        Output('by-year','figure'),
        Output('by-committee','figure'),
     ],
    [Input('url','pathname')],
    []
)
def generate_rep(pathname):
    tckact=dash.no_update
    yearapp=dash.no_update
    comapp=dash.no_update
    if pathname=="/generate-report":
        sql="SELECT app_batch,COUNT(*) from upciem_member WHERE True GROUP BY app_batch ORDER BY app_batch ASC;"
        values=[]
        cols=['Batch','Count']
        df=db.querydatafromdatabase(sql,values,cols)
        tckact=px.bar(df,x='Batch',y='Count',title='Total Active by App Batch')
        tckact.update_layout(xaxis=dict(dtick=1),yaxis=dict(dtick=1))
        sql="SELECT year_standing,COUNT(*) from upciem_member WHERE True GROUP BY year_standing ORDER BY year_standing ASC"
        values=[]
        cols=['Year','Count']
        df=db.querydatafromdatabase(sql,values,cols)
        yearapp=px.bar(df,x='Year',y='Count',title='Total Active by Year Standing',)
        yearapp.update_layout(xaxis=dict(dtick=1))
        sql="SELECT app_batch,COUNT(*) from upciem_member WHERE True GROUP BY app_batch;"
        values=[]
        cols=['com','Count']
        df=db.querydatafromdatabase(sql,values,cols)
        comapp=px.line(df,x='com',y='Count',title='Total Active by Committee',)
        comapp.update_layout(xaxis=dict(dtick=1),yaxis=dict(dtick=1))
        return [tckact,yearapp,comapp]

    raise PreventUpdate