import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from read_database import READ_DATABASE


class FIGURE:

    def __init__(self):
        self.db = READ_DATABASE()

    def create_card(self, target):
        big_number = self.db.read_global_status()[f'Total{target}']
        new_cases_number = self.db.read_global_status()[f'New{target}']

        card_figure = dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H6(str(target), className='card-title-f'),
                        html.P(f'{big_number:,}', className='card-big-number-f'),
                        html.P(f'New Cases: {new_cases_number:,}', className='card-new-cases-f')
                    ],
                    className='card-content'
                )
            ],
            className='card-figure-f'
        )

        return card_figure


    def create_map(self, target):
        df = self.db.df_countries_status()
        map_figure = go.Figure(
            data=go.Choropleth(
                locations=df['Country'],
                z=df[str(target)],
                locationmode='country names',
                colorscale='Burg',
                colorbar_title=str(target)
            ),
            layout=go.Layout(
                geo=dict(bgcolor='rgba(0,0,0,0)'),
                font={'size': 14, 'color': 'white'},
                margin={'r': 0, 't': 40, 'l':0, 'b': 0},
                paper_bgcolor='#4E5D6C',
                plot_bgcolor='#4E5D6C'
            )
        )

        return map_figure


if __name__ == '__main__':

    figure = FIGURE()

    # Initialize Dash app
    app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])

    # Set app layout
    app.layout = html.Div(
        [
            html.Div(
                [
                    html.P('🦠', className='emoji-f'),
                    html.H1('Coronavirus Tracker', className='header-title-f'),
                    html.P('Here you will find a series of visualizations describing the evolution of the coronavirus.',
                           className='header-description-f')
                ],
                className='header-container-f'
            ),
            dbc.Container(
                [
                    dbc.Container(
                        [
                            html.H1('Global Cases', className='cards-title-f'),
                            dbc.Row(
                                [
                                    dbc.Col(figure.create_card('Confirmed'), md=4),
                                    dbc.Col(figure.create_card('Deaths'), md=4),
                                    dbc.Col(figure.create_card('Recovered'), md=4)
                                ],
                                className='cards-figures-container'
                            )
                        ],
                        className='cards-container-f'
                    ),
                    dbc.Container(
                        [
                            html.H1('Global Map', className='graph-title-f'),
                            dcc.Dropdown(
                                id='map-filter-id',
                                options=[
                                    {'label': target, 'value': target} for target in [
                                        'TotalConfirmed', 'TotalDeaths', 'TotalRecovered',
                                        'NewConfirmed', 'NewDeaths', 'NewRecovered'
                                    ]
                                ],
                                value='TotalConfirmed',
                                clearable=False,
                                className='map-filter-f'
                            ),
                            dbc.Col(
                                [
                                    dbc.Col(
                                        dcc.Graph(id='map-figure-id', figure=figure.create_map('TotalConfirmed'))
                                    )
                                ],
                                className='map-figure-f',
                                align='center'
                            )
                        ],
                        className='global-graphs-container-f'
                    ),
                    dbc.Container(
                        [
                            html.P('Made in Colombia...', className='credits-text-f'),
                            html.P('By Bedo', className='credits-text-f')
                        ]
                    )
                ],
                fluid=True,
                className='background-f'
            )
        ],
        className='background-f'
    )

    @app.callback(
        Output('map-figure-id', 'figure'),
        Input('map-filter-id', 'value')
    )
    def update_map(target):

        return figure.create_map(str(target))


    app.run_server(debug=True)