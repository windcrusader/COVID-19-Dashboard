# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



dailycases = [5,6, 8, 9,12,20,28,
              39,52,66,102,155,205,283,
              368,451,514,589,647,708,797,
              868,950,1039,1106,1160,1210,1239,
             1283,1312,1330,1349,1366,1386,1401,
             1409,1422,1431,1440,1445,1451,1451,
             1456,1461,1470]
deaths = [0,0, 0, 0,0,0,0,
              0,0,0,0,0,0,0,
              0,0,1,1,1,1,1,
              1,1,1,1,1,1,1,
             2,4,4,5,9,9,9,
             11,11,12,12,13,14,16,
         17,18,18]
recoveries = [0, 0, 0, 0, 0, 0, 0, 
              0, 0, 0, 0, 12, 22, 27, 
              37, 50, 56, 63, 74, 83, 92, 
              103, 127, 156, 176, 241, 282, 317, 
              373, 422, 471, 546, 628, 728, 770,
              816, 867, 912,974,1006,1036,1065,
             1095,1118,1142]

active_cases = [t - r - d for t, r, d in zip(dailycases, recoveries, deaths)]

#make the x-axis dates
today = dt.datetime.now()
dates = []
minusday = dt.timedelta(days=1)
for i in range(len(dailycases)):
    dates.append(today - minusday*i)
dates_rev = list(reversed(dates))
x_bar = dates_rev[-6::]

app = dash.Dash(__name__,  external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(children='NZ COVID-19 Dashboard'),

 

    dcc.Graph(
        id='covidcases',
        figure={'data':[
            go.Bar(name='Active Cases', x=dates_rev, y=active_cases),
            go.Bar(name='Recoveries', x=dates_rev, y=recoveries),
            go.Bar(name='Deaths', x=dates_rev, y=deaths)
            ],

            'layout': {
                'title': 'NZ COVID-19 Cases, Recoveries and Deaths',
                'barmode': "stack"
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)