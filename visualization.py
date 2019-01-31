import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Load the data from the csv file
df = pd.read_csv('mpg.csv')

# Initialize the app
app = dash.Dash()

# Create a list of the columns ['mpg', 'weight', 'hp', etc]
features = df.columns

# Create the app layout
app.layout = html.Div([
  # div for the Y axis feature selector
  html.Div([
    html.H3('Y Axis'),
    dcc.Dropdown(id='yaxis',
                options=[{'label':i, 'value':i} for i in features],
                value='mpg')
  ], style={'width':'35%', 'display':'inline-block'}),
  # div for the X axis feature selector
  html.Div([
    html.H3('X Axis'),
    dcc.Dropdown(id='xaxis',
                options=[{'label':i, 'value':i} for i in features],
                value='displacement'),
  ], style={'width':'35%', 'display':'inline-block'}),
  dcc.Graph(id='feature-graphic')
], style={'padding':10})

# Link the two input selectors to the graph
@app.callback(Output('feature-graphic', 'figure'),
             [Input('xaxis', 'value'),
              Input('yaxis', 'value')])

# Create a function that returns the figure dictionary that goes into the graph
def update_graph(xaxis_name, yaxis_name):
  return {'data':[go.Scatter(x=df[xaxis_name], 
                            y=df[yaxis_name],
                            text=df['name'],
                            mode='markers',
                            marker={'size':15, 'opacity':0.6, 'line':{'width':0.5, 'color': 'white'}})],
          'layout': go.Layout(title='Comparing Relationships Between Different Car Features',
                              xaxis={'title': xaxis_name},
                              yaxis={'title': yaxis_name},
                              hovermode='closest')}

if __name__ == '__main__':
  app.run_server()
