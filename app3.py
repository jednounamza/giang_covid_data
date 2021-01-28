import dash
import dash_core_components as dcc
import dash_html_components as html
import pycountry
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

DATASET = r'/home/h31bnj24/3/97/data1.csv'
df1 = pd.read_csv(DATASET)
print(df1.head(4))  # I get first 4 entries in the dataframe
print(df1.tail(4))  # I get last 4 entries in the dataframe

df1=df1.fillna(0)

list_countries = df1['countriesAndTerritories'].unique().tolist()
 
fig1 = px.choropleth(data_frame = df1.sort_values(by='year_week'),
                    locations= "countryterritoryCode",
                    color= "cases_weekly",  # value in column determines color
                    hover_name= "countriesAndTerritories",
                    color_continuous_scale= 'RdYlGn',  #  color scale red, yellow green
                    animation_frame= "dateRep")
fig2 = px.choropleth(data_frame = df1.sort_values(by='year_week'),
                    locations= "countryterritoryCode",
                    color= "deaths_weekly",  # value in column determines color
                    hover_name= "countriesAndTerritories",
                    color_continuous_scale= 'RdYlGn',  #  color scale red, yellow green
                    animation_frame= "dateRep")
fig3 = px.choropleth(data_frame = df1.sort_values(by='year_week'),
                    locations= "countryterritoryCode",
                    color= "notification_rate_per_100000_population_14-days",  # value in column determines color
                    hover_name= "countriesAndTerritories",
                    color_continuous_scale= 'RdYlGn',  #  color scale red, yellow green
                    animation_frame= "dateRep") 
                                                        
fig11 = px.histogram(df1.sort_values(by='year_week'), x="dateRep", y="cases_weekly", histfunc='sum')
fig22 = px.histogram(df1.sort_values(by='year_week'), x="dateRep", y="deaths_weekly", histfunc='sum')
fig33 = px.histogram(df1.sort_values(by='year_week'), x="dateRep", y="notification_rate_per_100000_population_14-days", histfunc='avg')
#fig.show()    
def get_options(list_c):
    dict_list = []
    for i in list_c:
        dict_list.append({'label': i, 'value': i})

    return dict_list

app.layout = html.Div(children=[
    html.H1(children='COVID-19 cases worldwide'),

    html.Div(children='''
        Dash: cases_weekly World
    '''),   
    dcc.Graph(
        id='example-graph1',
        figure=fig1                  
    ),
                                         
    html.Div(id='dd-output-container'),      
    dcc.Graph(
        id='example-graph11',
        figure=fig11          
    ),
    html.Div(children='''
        Dash: cases_weekly 
    '''),   
    dcc.Dropdown(id='demo-dropdown',
                 options=get_options(df1['countriesAndTerritories'].unique()),
                           multi=False,
                           value=[df1['countriesAndTerritories'].sort_values()[0]],
                           style={'backgroundColor': '#FFFFFF'},
                           className='stockselector'
                          ),                   
    html.Div(id='dd-output-container111'),      
    dcc.Graph(
        id='example-graph111'
    ),
    html.Div(children='''
        Dash: deaths_weekly World
    '''),
    dcc.Graph(
        id='example-graph2',
        figure=fig2                  
    ),
    html.Div(children='''
        Dash: deaths_weekly World
    '''),
    dcc.Graph(
        id='example-graph22',
        figure=fig22                  
    ),
    html.Div(children='''
        Dash: deaths_weekly
    '''),   
    dcc.Dropdown(id='demo-dropdown2',
                 options=get_options(df1['countriesAndTerritories'].unique()),
                           multi=False,
                           value=[df1['countriesAndTerritories'].sort_values()[0]],
                           style={'backgroundColor': '#FFFFFF'},
                           className='stockselector'),  
    html.Div(id='dd-output-container222'),      
    dcc.Graph(
        id='example-graph222'
    ),
    html.Div(children='''
        Dash: notification_rate_per_100000_population_14-days World
    '''),
    dcc.Graph(
        id='example-graph3',
        figure=fig3                  
    ),
    html.Div(children='''
        Dash: notification_rate_per_100000_population_14-days World
    '''),    
    dcc.Graph(
        id='example-graph33',
        figure=fig33
    ),    
    html.Div(children='''
        Dash: notification_rate_per_100000_population_14-days
    '''),   
    dcc.Dropdown(id='demo-dropdown3',
                 options=get_options(df1['countriesAndTerritories'].unique()),
                           multi=False,
                           value=[df1['countriesAndTerritories'].sort_values()[0]],
                           style={'backgroundColor': '#FFFFFF'},
                           className='stockselector'),  
    html.Div(id='dd-output-container333'),      
    dcc.Graph(
        id='example-graph333'                
    ) 
])

@app.callback(
    dash.dependencies.Output('example-graph111', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])    
def update_output(value):
    vvv=''.join(value)
    if vvv=='Afghanistan':
                         value='Afghanistan'
    df_sub = df1.sort_values(by='year_week')    
    figure = px.histogram(df_sub[df_sub['countriesAndTerritories'] == value], x="dateRep", y="cases_weekly")   
    return figure

@app.callback(
    dash.dependencies.Output('example-graph222', 'figure'),
    [dash.dependencies.Input('demo-dropdown2', 'value')])    
def update_output(value):
    vvv=''.join(value)
    if vvv=='Afghanistan':
                         value='Afghanistan'
    df_sub = df1.sort_values(by='year_week') 
    figure = px.histogram(df_sub[df_sub['countriesAndTerritories'] == value], x="dateRep", y="deaths_weekly")  
    return figure

@app.callback(
    dash.dependencies.Output('example-graph333', 'figure'),
    [dash.dependencies.Input('demo-dropdown3', 'value')])    
def update_output(value):
    vvv=''.join(value)
    if vvv=='Afghanistan':
                         value='Afghanistan'
    df_sub = df1.sort_values(by='year_week') 
    figure = px.histogram(df_sub[df_sub['countriesAndTerritories'] == value], x="dateRep", y="notification_rate_per_100000_population_14-days")  
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)

    
