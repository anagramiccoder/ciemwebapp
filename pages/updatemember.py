
from dash import html,dash_table,dcc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from app import app
from apps import dbconnect as db
navigationpanel = html.Nav([html.Div([
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
        html.A("Update Member Status", href="#",className="disabled-a"),
        html.A("Update Alumni Status", href="/update-alumni",),
        html.A("Managers", href="/managers",),
    ],className="module-div"),
    html.Div([
        html.H4("Generation"),
        html.A("Generate Report", href="/generate-report",),
    ],className="module-div"),
],className="nav")

sectionbody=html.Div([
    html.H2("Update Members"),
        html.Div([html.H5("Search Name"),
        dcc.Input(
            type='text',
            className='searchbar',
            id='uns'
        )],className='flex half'),
    html.Div(id="update_mem",
        className="dt"),
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
Output('update_mem', 'children')
],
[
Input('url', 'pathname'),
Input('uns','value'),
]
)
def members(pathname,namesearch):
    if pathname=="/update-member":
        sql="""
        SELECT member_id,(first_name||' '||middle_name||' '||last_name||' '||suffix) as full_name,membership_type
        from PERSON join upciem_member 
        ON person.valid_id=upciem_member.valid_id
        WHERE True
            """
        values=[]
        cols=["Member ID","Name","Membership Type"]
        if namesearch:
            sql+="""AND (first_name||' '||middle_name||' '||last_name||' '||suffix) ILIKE %s"""
            values+={f"%{namesearch}%"}
        df = db.querydatafromdatabase(sql, values, cols)
        df['Action'] = [f'<a href="/update-member-modify?mode=edit&id={id}" ><Button class="lbtn">Edit</Button></a>' for id in df['Member ID']]
        table=dash_table.DataTable(
        data=df.to_dict('records'),  # Convert DataFrame to list of dictionaries
        columns=[{'name': i, 'id': i, 'presentation': 'markdown'} if i == 'Action' else {'name': i, 'id': i} for i in df.columns],  # Specify column names and IDs
        markdown_options={'html': True},
        style_cell={
            "height":"50px",
            'text-align':'left',
            "background-color":"#EEF2FA",
            "color":"#273250",
            },
        style_header={
            "background-color":"#000097",
            "color":"#FFF",
            "text-align":"center",
            "border-bottom":"4px solid white",
            },
        page_action='native',
        page_size=10,
        style_table={"height":"80%",'overflow':'hidden'},
)
        return [table]
    else:
        raise PreventUpdate