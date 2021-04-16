import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import webbrowser
from threading import Timer
from main import Data

data = Data()
global_data = data.get_actual_global_data()
map_data = data.get_all_countries_actual_data()
df_map = pd.DataFrame(map_data)


def create_card(data, target):
    big_number_value = data['Total'+str(target)]
    new_cases_value = data['New'+str(target)]

    card_fig = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H6(children=str(target), className='card-title-style'),
                    html.P(f'{big_number_value:,}', className='card-big-number-style'),
                    html.P(f'New Cases: +{new_cases_value:,}', className='card-new-cases-style')
                ]
            )
        ],
        className='card-item'
    )

    return card_fig


def create_map(df, target):
    map_fig = go.Figure(
                    data=go.Choropleth(
                    locations=df['Country'],
                    z = df[str(target)],
                    locationmode = 'country names',
                    colorscale = 'Burg',
                    colorbar_title = str(target),
                ),
                    layout = go.Layout(
                    geo=dict(bgcolor= 'rgba(0,0,0,0)'),
                    font = {"size": 14, "color":"White"},
                    margin={"r":0,"t":40,"l":0,"b":0},
                    paper_bgcolor='#4E5D6C',
                    plot_bgcolor='#4E5D6C',
                )
            )

    return map_fig


app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])

app.layout = html.Div(
    [
        html.Div(
            [
                html.P('🦠', className='header-emoji'),
                html.H1('Coronavirus Tracker', className='header-title'),
                html.P('In this section you will find a series of visualizations describing the evolution of the coronavirus.', className='header-description')
            ],
            className='header-container',
        ),
        dbc.Container(
            [
                dbc.Container(
                    [
                        html.H1('Global Cases', className='header-global-title'),
                        dbc.Row(
                            [
                                dbc.Col(create_card(global_data, 'Confirmed'), md=4),
                                dbc.Col(create_card(global_data, 'Deaths'), md=4),
                                dbc.Col(create_card(global_data, 'Recovered'), md=4)
                            ]
                        )
                    ],
                    className='cards-container'
                ),
                dbc.Container(
                    [
                        html.H1('Global Map', className='map-title-2'),
                        dcc.Dropdown(
                            id='map-data-filter',
                            options=[
                                {'label': concept, 'value': concept}
                                for concept in ['TotalConfirmed', 'TotalDeaths', 'TotalRecovered',
                                                'NewConfirmed', 'NewDeaths', 'NewRecovered']
                            ],
                            value='TotalConfirmed',
                            clearable=False,
                            className='map-filter'
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(id='map-figure', figure=create_map(df_map, 'TotalConfirmed'))
                                )
                            ],
                            className='map',
                            align='center'
                        )
                    ],
                    className='map-figure-container'
                ),
                dbc.Container(
                    [
                        html.P('Made in Colombia...', className='credits-text'),
                        html.P('By Bedo', className='credits-text')
                    ]

                )
            ],
            fluid=True,
            className='background'
        )
    ],
    className='background'
)

@app.callback(
    Output('map-figure', 'figure'),
    Input('map-data-filter', 'value')
)
def update_map(concept):
    figure = create_map(df_map, str(concept))

    return figure


port = 8050 # or simply open on the default `8050` port

def open_browser():
	webbrowser.open_new("http://localhost:{}".format(port))


if __name__ == "__main__":
    Timer(1, open_browser).start();
    app.run_server(debug=True)