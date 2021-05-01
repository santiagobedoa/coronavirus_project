import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from graphs import FIGURE


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
                                    dbc.Col(figure.global_status_card('Confirmed'), md=4),
                                    dbc.Col(figure.global_status_card('Deaths'), md=4),
                                    dbc.Col(figure.global_status_card('Recovered'), md=4)
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
                                id='map-dropdown-id',
                                options=[
                                    {'label': target, 'value': target} for target in [
                                        'TotalConfirmed', 'TotalDeaths', 'TotalRecovered',
                                        'NewConfirmed', 'NewDeaths', 'NewRecovered'
                                    ]
                                ],
                                value='TotalConfirmed',
                                clearable=False,
                                className='map-dropdown-f'
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
        Input('map-dropdown-id', 'value')
    )
    def update_map(target):

        return figure.create_map(str(target))


    app.run_server(debug=True)