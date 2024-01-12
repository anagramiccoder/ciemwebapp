
from dash import html
navigationpanel = html.Nav([html.Div([
        html.H4("Main"),
        html.A("Home", href="#",className="disabled-a"),
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
        html.A("Managers", href="#",),
    ],className="module-div"),
    html.Div([
        html.H4("Generation"),
        html.A("Generate Report", href="/generate-report",),
    ],className="module-div"),
],className="nav")

sectionbody=html.Div([
    html.H2("This is the Homepage")
],className="body")
layout=html.Div([
        html.Div([html.A([html.Div([html.Img(src="./assets/logo.png",className="logo"),html.H2("UP CEIM")],className="flex center")],href="/home")],className="topbar"),
        html.Div([
            navigationpanel, 
            sectionbody,
            ],
            className='flex container'),])