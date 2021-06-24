import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Reading in NBA team stats
df = pd.read_csv("nba_game_stats.csv")

team_list = [team for team in set(df['TEAM_NAME'].tolist())]

team_options_dict_list = []

seasons_list = list(set([int(str(season)[-4:]) for season in df["SEASON_ID"].tolist()]))

seasons_options_dict_list = []

for team in team_list:
    team_options_dict_list.append({"label":team, 'value':team})

for season in seasons_list:
    seasons_options_dict_list.append({"label":str(season), "value":season})

# APP LAYOUT
app.layout = html.Div([

    html.H1("NBA Team Statistics (1983-2020) Dashboard", style={"text-align" : "center"}),

    dcc.Dropdown(id="select_team",
                 options=team_options_dict_list,
                 multi=False,
                 value='Boston Celtics',
                 style={'width': '40%'}
                 ),
    
    dcc.Dropdown(id="select_season",
                 options=seasons_options_dict_list,
                 multi=False,
                 value='Boston Celtics',
                 style={'width': '40%'}
                 ),

    html.Div(id='output_container', children=[]),
    html.br,

    dcc.Graph(id='season_totals')
])

# RUN APP
if __name__ == '__main__':
    app.run_server(debug=True)