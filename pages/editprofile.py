from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from datetime import date,datetime
from apps import dbconnect as db
from app import app
navigationpanel = html.Nav([html.Div([
        html.H4("Main"),
        html.A("Home", href="/home",),
        html.A("Logout", href="#",),
    ],className="module-div"),
    html.Div([
        html.H4("Profile"),
        html.A("Edit Profile", href="#",className="disabled-a"),
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
        html.A("Managers", href="/managers",),
    ],className="module-div"),
    html.Div([
        html.H4("Generation"),
        html.A("Generate Report", href="/generate-report",),
    ],className="module-div"),
],className="nav")

sectionbody=html.Div([
    html.H2("Edit Profile"),
    html.Div([
        html.Div([
            html.H3("First Name:"),dcc.Input(type='text', id='edit-fname'),
            html.H3("Middle Name:"),dcc.Input(type='text', id='edit-mname'),
            html.H3("Last Name:"),dcc.Input(type='text', id='edit-lname'),
            html.H3("Suffix:"),dcc.Input(type='text', id='edit-sfx'),
            ],className='flex edit name'),
            
        html.Div([
            html.H3("Birthday:"),dcc.DatePickerSingle(id='edit-bday',min_date_allowed=date(1940,1,1),display_format="YYYY-MM-DD"),
            html.H3("Contact Number:"),dcc.Input(type='text', id='edit-cn'),
            html.H3("Emergency Contact Number:"),dcc.Input(type='text', id='edit-ecn'),
            ],className='flex edit others'),
        html.Div([ 
            html.Div([html.H3("Email Address:"),dcc.Input(type='text', id='edit-email'),html.H3("Valid ID:"),dcc.Input(type='text',id='edit-vid')],className='flex add'),
            html.Div([html.H3("Present Address:"),dcc.Input(type='text', id='edit-presadd',),],className='flex add'),
            html.Div([html.H3("Permanent Address:"),dcc.Input(type='text', id='edit-permadd',)],className='flex add'),
            ],className='address'),
        html.Div([html.Button("Update Profile",id='up-prof-btn',n_clicks=0)],className='flex last')
    ],className='edit'),
],className="body")
layout=html.Div([
    html.Div([
    html.Label(className='hidden modal-background',id='ep-bg'),
    html.Div([
        html.Div(
            [html.H3("Action Done")],className='modal-header'
        ),
        html.P("Successfully Edited the Profile"),
        html.A([html.Button("Proceed",className='enter')],href='/edit-profile')
    ],className='hidden modal',id='ep-main')
]),
        html.Div([html.A([html.Div([html.Img(src="./assets/logo.png",className="logo"),html.H2("UP CEIM")],className="flex center")],href="/home")],className="topbar"),
        html.Div([
            navigationpanel, 
            sectionbody,
            ],
            className='flex container'),])
@app.callback(
[
    Output('edit-fname','value'),
    Output('edit-mname','value'),
    Output('edit-lname','value'),
    Output('edit-sfx','value'),
    Output('edit-bday','date'),
    Output('edit-cn','value'),
    Output('edit-ecn','value'),
    Output('edit-email','value'),
    Output('edit-vid','value'),
    Output('edit-presadd','value'),
    Output('edit-permadd','value'),

],
[
    Input('url','pathname'),
],
[
    State('auth','data')
]
)
def populate_info(pathname, data):
    if pathname=="/edit-profile":
        id=data['acc']
        sql="""
SELECT first_name,middle_name,last_name,suffix,birthdate,contact_number,emergency_contact_number,email,valid_id,present_address,permanent_address 
from person where account_id=
"""
        sql+=id
        values=[]
        cols=['fname','mname','lname','sfx','bday','cn','ecn','em','vid','pradd','peadd']
        df = db.querydatafromdatabase(sql, values, cols)
        if df.shape[0]:
            return df['fname'][0],df['mname'][0],df['lname'][0],df['sfx'][0],df['bday'][0], df['cn'][0],df['ecn'][0],df['em'][0],df['vid'][0],df['pradd'][0],df['peadd'][0]
        raise PreventUpdate
    else:
        raise PreventUpdate
@app.callback(
    [Output('ep-main','className'),
     Output('ep-bg','className')
     ],
     [Input('up-prof-btn','n_clicks')],
     [
         State('edit-fname','value'),
    State('edit-mname','value'),
    State('edit-lname','value'),
    State('edit-sfx','value'),
    State('edit-bday','date'),
    State('edit-cn','value'),
    State('edit-ecn','value'),
    State('edit-email','value'),
    State('edit-vid','value'),
    State('edit-presadd','value'),
    State('edit-permadd','value'),
    State('auth','data'),
     ]
)
def edit_prof(btn,fname,mname,lname,sfx,bday,cn,ecn,email,vid,presadd,permadd,data):
    if btn>0:
        print(bday)
        sql="""
            UPDATE person
            SET
            first_name=%s,
            middle_name=%s,
            last_name=%s,
            suffix=%s,
            birthdate=%s,
            contact_number=%s,
            emergency_contact_number=%s,
            email=%s,
            valid_id=%s,
            present_address=%s,
            permanent_address=%s
            WHERE account_id=
            """
        sql+=data['acc']
        values=[fname,mname,lname,sfx,bday,cn,ecn,email,vid,presadd,permadd]
        db.modifydatabase(sql,values)
        return 'shown modal','shown modal-background'
    raise PreventUpdate