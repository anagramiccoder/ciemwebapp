from app import app
from dash import html,Output,Input
import dash
from dash.exceptions import PreventUpdate
navigationpanel = html.Nav(
    [
        html.Div(
            [
            html.H4("Main"),
            html.A("Home", href="/home", id='home'),
            html.A("Logout", href="#",id='lo',n_clicks=0),
            ],className="module-div"),
        html.Div(
            [
            html.H4("Profile"),
            html.A("Edit Profile", href="/edit-profile",id='edit'),
            html.A("Change Password", href="/change-password",id='change'),
            ],className="module-div"),
        html.Div(
            [
            html.H4("Reaffilation"),
            html.A("Reaffilation Form",href="/reaffiliate",id='reaff'),
            ],className="module-div"),
        html.Div(
            [
            html.H4("Members"),
            html.A("All Members", href="/members",id='members'),
            ],className="module-div"),
        html.Div(
            [
            html.H4("Alumni"),
            html.A("All Alumni", href="/alumni",id='alumns'),
            ],className="module-div"),
        html.Div(
            [
            html.H4("Account Management"),
            html.A("Update Member Status", href="/update-member",id='update-mems'),
            html.A("Update Alumni Status", href="/update-alumni",id='update-alums'),
            html.A("Managers", href="/managers?mode=view",id='managers'),
            ],className="module-div"),
        html.Div([
            html.H4("Generation"),
            html.A("Generate Report", href="/generate-report",id='tracks'),
            ],className="module-div"),
    ],
className="nav")

@app.callback(
    [
        Output('home','className'),
        Output('edit','className'),
        Output('change','className'),
        Output('reaff','className'),
        Output('members','className'),
        Output('alumns','className'),
        Output('update-mems','className'),
        Output('update-alums','className'),
        Output('managers','className'),
        Output('tracks','className'),
     ],
     [Input('url','pathname')]
)
def current_page(pathname):
    h=dash.no_update
    e=dash.no_update
    c=dash.no_update
    r=dash.no_update
    m=dash.no_update
    a=dash.no_update
    um=dash.no_update
    ua=dash.no_update
    mg=dash.no_update
    tr=dash.no_update
    if pathname == '/' or pathname == '/home':
        h='disabled-a'
    elif pathname=="/change-password":
        c='disabled-a'
    elif pathname=="/edit-profile":
        e='disabled-a'
    elif pathname=="/generate-report":
        tr='disabled-a'
    elif pathname=="/managers":
        mg='disabled-a'
    elif pathname=="/members":
        m='disabled-a'
    elif pathname=="/reaffiliate":
        r='disabled-a'
    elif pathname=="/update-alumni":
        ua='disabled-a'
    elif pathname=="/update-member" or pathname=="/update-member-modify":
        um='disabled-a'
    elif pathname=="/alumni":
        a='disabled-a'
    return h,e,c,r,m,a,um,ua,mg,tr
top=html.Div([html.A([html.Div([html.Img(src="./assets/logo.png",className="logo"),html.H2("UP CEIM")],className="flex center")],href="/home")],className="topbar")
       