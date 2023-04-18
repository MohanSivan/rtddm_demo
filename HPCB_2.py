from tkinter.ttk import Style
import dash
#import dash_core_components as dcc
from dash import dcc,html,dash_table
#import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
#import dash_daq as daq
#from pyorbital.orbital import Orbital

#Read_Excell file_formet with Add Column Names:
col_names=['Description', 'Machine', 'Readings', 'Datetime']
df1 = pd.read_excel(r"test.xlsx",names=col_names, header=None)
#mydataset="https://github.com/MohanSivan/rtddm_demo/RTDataCapture(01).xlsx"
#df1 = pd.read_excel(mydataset,names=col_names, header=None)
#All Machine Count:
Total_Machine_Counts = df1.Machine.nunique()
#print(df1.Machine.nunique())
#Shift Runing Time :
filterkey_B=["B.Run Time in Min"]
cleardf1=df1[df1.iloc[:,0].isin(filterkey_B)]
cleardfB=(cleardf1.iloc[0:1000, [2]].sum())
Total_Sft_Rt = cleardf1.Readings.sum()
Avg_Toatal_Sft_Rt = ( Total_Sft_Rt / Total_Machine_Counts)
#print(Avg_Toatal_Sft_Rt)
#print(Total_Sft_Rt)
#print((cleardf1.Readings.sum())  / (df1.Machine.nunique()*480)*100)

#Shift Idle Time :
filterkey_C=["C.Idle Time in Min"]
cleardf2=df1[df1.iloc[:,0].isin(filterkey_C)]
Total_Sft_It = cleardf2.Readings.sum()
Avg_Toatal_Sft_It = ( Total_Sft_It / Total_Machine_Counts)

#print(Total_Sft_It)
#print(Avg_Toatal_Sft_It)
#print((cleardf2.Readings.sum())  / (df1.Machine.nunique()*480)*100)

#Shift Deadlock Time :
filterkey_D=["D.DeadLock Time in Min"]
cleardf3=df1[df1.iloc[:,0].isin(filterkey_D)]
Total_Sft_Dt = cleardf3.Readings.sum()
Avg_Toatal_Sft_Dt = ( Total_Sft_Dt / Total_Machine_Counts)
#print(Avg_Toatal_Sft_Dt)
#print(Total_Sft_Dt)
#print((cleardf3.Readings.sum())  / (df1.Machine.nunique()*480)*100)

#Shift Break Down Time :
filterkey_E=["E.Break Down Time in Min"]
cleardf4=df1[df1.iloc[:,0].isin(filterkey_E)]
Total_Sft_BDt = cleardf4.Readings.sum()
Avg_Toatal_Sft_BDt = ( Total_Sft_BDt / Total_Machine_Counts)
#print(Avg_Toatal_Sft_BDt)
#print(Total_Sft_BDt)
#print((cleardf4.Readings.sum())  / (df1.Machine.nunique()*480)*100)

#Actual Outputs :
filterkey_F=["F.Actual Outputs"]
cleardf5=df1[df1.iloc[:,0].isin(filterkey_F)]
Total_Act_Outputs = cleardf5.Readings.sum()
Avg_Toatal_Act_Outputs = ( Total_Act_Outputs / Total_Machine_Counts)
#print(Avg_Toatal_Act_Outputs)
#print(Total_Act_Outputs)
#print((cleardf5.Readings.sum())  / (df1.Machine.nunique()*480)*100)

#Machine Utilization :
filterkey_I=["I.Machine Utilization %"]
cleardf6=df1[df1.iloc[:,0].isin(filterkey_I)]
Total_Utilization = cleardf6.Readings.sum()
Avg_Total_Utilization = ( Total_Utilization / Total_Machine_Counts)
#print(Avg_Total_Utilization)
#print(Total_Utilization)
#print((cleardf6.Readings.sum())  / (df1.Machine.nunique()))

#Target Efficiency :
filterkey_J=["J.Target Efficiency %"]
cleardf7=df1[df1.iloc[:,0].isin(filterkey_J)]
Target_Eff = cleardf7.Readings.sum()
Avg_Target_Eff = ( Target_Eff / Total_Machine_Counts)
#print(Avg_Target_Eff )
#print(Target_Eff)
#print((cleardf7.Readings.sum())  / (df1.Machine.nunique()))

#Pie Chart:
filterkey=["B.Run Time in Min","C.Idle Time in Min","D.DeadLock Time in Min","E.Break Down in Min"]
cleardf8=df1[df1.Description.isin(filterkey)]

df = pd.DataFrame(df1)

df.to_csv(r'RTTDM_Dataexport_dataframe.csv', index=False, header=True)

df.to_excel(r'RTTDM_Data\.%d%Y%H%.xlsx', index=False)


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout=html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('A_R_Logo-removebg-preview.png'),
                     id='AR-image',
                     style={
                         "height": "100px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
                     )
        ],className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("RTDDM", style={"margin-bottom": "2px", 'color': 'Yellow'}),
                html.H3("High Post Bed Machine Data", style={"margin-top": "1px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title"),

        html.Div([
                html.H6('Last Updated: '+ str(df1['Datetime'].iloc[-1].strftime("%B %d,%Y %H:%M")),
                    style={'color': 'orange'}),
       ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

        html.Div([
            html.Div([
                html.H6(children='Total Machines',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                html.P(f"{df1.Machine.nunique()}" ,
                        style={
                            'textAlign': 'center',
                            'color': 'orange',
                            'fontSize': 20}
                        )
                    ],className="card_container three columns",
                    ),
            html.Div([
                html.H6(children='Actual Outputs',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                html.P(f"{((cleardf5.Readings.sum()) / (df1.Machine.nunique()*250)*100):,.2f}" + '%',
                        style={
                            'textAlign': 'center',
                            'color': 'orange',
                            'fontSize': 20}
                        )
                    ],className="card_container three columns",
                    ),
            html.Div([
                html.H6(children='Total Utilizations',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                html.P(f"{((cleardf6.Readings.sum()) / (df1.Machine.nunique())):,.2f}" + '%',
                        style={
                            'textAlign': 'center',
                            'color': 'orange',
                            'fontSize': 20}
                        )
                    ],className="card_container three columns",
                    ),
            html.Div([
                html.H6(children='Target Efficiency',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                html.P(f"{((cleardf7.Readings.sum()) / (df1.Machine.nunique())):,.0f}" + '%',
                        style={
                            'textAlign': 'center',
                            'color': 'orange',
                            'fontSize': 20}
                        )
                    ],className="card_container three columns",
                    )
            ],className="row flex-display",),

        html.Div([
            html.Div([
                html.H6(children='Run Time : '+ str(Avg_Toatal_Sft_Rt),
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(f"{((cleardf1.Readings.sum()) / (df1.Machine.nunique()*480)*100):,.2f}" + '%',
                    style={
                        'textAlign': 'center',
                        'color': 'orange',
                        'fontSize': 20}
                    )
                ],className="card_container three columns",
                ),

            html.Div([
                html.H6(children='Idle Time : '+ str(Avg_Toatal_Sft_It),
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(f"{((cleardf2.Readings.sum()) / (df1.Machine.nunique()*480)*100):,.2f}" + '%',
                    style={
                        'textAlign': 'center',
                        'color': 'orange',
                        'fontSize': 20}
                    )
                ],className="card_container three columns",
                ),

            html.Div([
                html.H6(children='Deadlock Time : '+ str(Avg_Toatal_Sft_Dt),
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(f"{((cleardf3.Readings.sum()) / (df1.Machine.nunique()*480)*100):,.2f}" + '%',
                    style={
                        'textAlign': 'center',
                        'color': 'orange',
                        'fontSize': 20}
                    )
                ],className="card_container three columns",
                ),
            html.Div([
                html.H6(children='Break Down Time : '+ str(Avg_Toatal_Sft_BDt),
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(f"{((cleardf4.Readings.sum()) / (df1.Machine.nunique()*480)*100):,.2f}" + '%',
                    style={
                        'textAlign': 'center',
                        'color': 'orange',
                        'fontSize': 20}
                    )
                ],className="card_container three columns",
                )
            ],className="row flex-display",
        )
    ]),
        html.Div([
            html.Div([
                dcc.Dropdown(id='Description-Choice',
                options=[{'label':x, 'value':x}
                          for x in sorted(cleardf8.Description.unique())],
                value='B.Run Time in Min',className="row flex-display"),
            
                dcc.Graph(id='my-graph',
                figure={})
            ],className="create_container five columns",)
     ]),
            html.Div([
                dcc.Dropdown(id='Machine-Choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(cleardf8.Machine.unique())],
                 value='SEW000004030',className="row flex-display"),
                
                dcc.Graph(id='my-graph1',
                figure={})
            ],className="create_container five columns",)

])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='Description-Choice', component_property='value')
  ) 
def interactive_graphs(value_genre):
    #print(value_genre)
    cleardf9=cleardf8[cleardf8.Description==value_genre]
    fig = px.bar(data_frame=cleardf9,x='Machine',y='Readings')
    return fig

@app.callback(
    Output(component_id='my-graph1', component_property='figure'),
    Input(component_id='Machine-Choice', component_property='value')
  ) 

def interactive_graphs(value_genre1):
    #print(value_genre1)
    cleardf10= cleardf8[cleardf8.Machine==value_genre1]
    fig = px.pie(data_frame=cleardf10, names='Description',values='Readings')
    return fig

if __name__=='__main__':
    app.run_server(debug=True)

#if __name__ == '__main__':
    #ADDRESS='192.168.7.55'  #ipv4 address for computer code is run on
    #PORT=int(1000)
    #app.run_server(debug=True, host=ADDRESS, port=PORT)