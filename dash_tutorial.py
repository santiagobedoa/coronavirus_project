# pip install dash
# pip install pandas
# pip install dash-bootstrap-components: to do the Cards (global cases...) but first try go.Indicators

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime

global_data = {'NewConfirmed': 198996, 'TotalConfirmed': 131539636, 'NewDeaths': 3923, 'TotalDeaths': 2857906, 'NewRecovered': 119884, 'TotalRecovered': 74751948, 'Date': datetime.datetime(2021, 4, 6, 7, 3, 37, 654000)}
df = pd.DataFrame.from_dict(list(global_data.items()))
df.columns = ['Concept', 'Value']


def create_card(value, text):
    fig = go.Figure(go.Indicator(
        value = value,
        title = {"text": str(text)}
    ))

    fig.update_layout(paper_bgcolor = "lightgray", height= 200)

    return fig


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'Coronavirus Tracker' # what appears on tab and google search

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children='🦠', className='header-emoji'),
                html.H1(children='Coronavirus Tracker', className='header-title'),
                html.P(children='Bring a series of visualizations about the coronavirus crisis evolution', className='header-description')
            ],
            className='header',
        ),
        #
        html.Div(
            children=[
                html.H1(children='Global Cases', className='header-title-global'),
                html.Div(
                    children=[
                        html.Div(
                            children=(
                                dcc.Graph(
                                    id= 'Total_Confirmed',
                                    figure=create_card(global_data['TotalConfirmed'], 'Total Confirmed')
                                ),
                            ),
                            className='card',
                        ),
                        html.Div(
                            children=(
                                dcc.Graph(
                                    id= 'Total_Deaths',
                                    figure=create_card(global_data['TotalDeaths'], 'Total Deaths')
                                )
                            ), className='card'
                        ),
                        html.Div(
                            children=(
                                dcc.Graph(
                                    id='Total_Recovered',
                                    figure=create_card(global_data['TotalRecovered'], 'Total Recovered')
                                )
                            ), className='card'
                        ),
                    ],
                    style={'columnCount': 3},
                    className='wrapper'
                )
            ],
            className='wrapper'
        ),
        # html.Div(
        #     children=[
        #         html.Div(
        #             children=(
        #                 dcc.Graph(
        #                     id= 'Total_Confirmed',
        #                     figure=create_card(global_data['TotalConfirmed'], 'Total Confirmed')
        #                 ),
        #             ),
        #             className='card',
        #         ),
        #         html.Div(
        #             children=(
        #                 dcc.Graph(
        #                     id= 'Total_Deaths',
        #                     figure=create_card(global_data['TotalDeaths'], 'Total Deaths')
        #                 )
        #             ), className='card'
        #         ),
        #         html.Div(
        #             children=(
        #                 dcc.Graph(
        #                     id='Total_Recovered',
        #                     figure=create_card(global_data['TotalRecovered'], 'Total Recovered')
        #                 )
        #             ), className='card'
        #         ),
        #     ],
        #     style={'columnCount': 3},
        #     className='wrapper'
        # ),
        html.Div(
            children=[
                html.Div(
                    children=(
                        dcc.Graph(
                            id='New_confirmed',
                            figure=create_card(global_data['NewConfirmed'], 'New Confirmed')
                        ),
                    ),
                    className='card',
                ),
                html.Div(
                    children=(
                        dcc.Graph(
                            id='New_Deaths',
                            figure=create_card(global_data['NewDeaths'], 'New Deaths')
                        )
                    ), className='card'
                ),
                html.Div(
                    children=(
                        dcc.Graph(
                            id='New_Recovered',
                            figure=create_card(global_data['NewRecovered'], 'New Recovered')
                        )
                    ), className='card'
                ),
            ],
            style={'columnCount': 3},
            className='wrapper'
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)