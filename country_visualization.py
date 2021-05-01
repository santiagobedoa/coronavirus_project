import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from graphs import FIGURE
from read_database import READ_DATABASE

if __name__ == '__main__':

    read_database = READ_DATABASE()
    figure = FIGURE()

    country = 'Colombia'

    app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])

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
                            html.H1(country.upper(), className='country-name-f'),
                            html.P('Active Cases:', className='country-active-cases-f'),
                            html.P(f'{read_database.country_historical_data(country)[-1]["Active"]:,}', className='country-active_cases-num-f'),
                            dbc.Row(
                                [
                                    dbc.Col(figure.country_status_card(country, 'Confirmed'), md=4),
                                    dbc.Col(figure.country_status_card(country, 'Deaths'), md=4),
                                    dbc.Col(figure.country_status_card(country, 'Recovered'), md=4)
                                ],
                                className='cards-container-f'
                            )
                        ]
                    ),
                    dbc.Container(
                        [
                            html.H1('Linear Chart', className='graph-title-f'),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dcc.Graph(
                                            id='linear_chart_figure',
                                            figure=figure.linear_chart(country, 'NewConfirmed')
                                        ),
                                        md=10
                                    ),
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id='linear_chart_dropdown',
                                            options=[
                                                {'label': target, 'value': target}
                                                for target in (
                                                    ['NewConfirmed', 'NewDeaths', 'NewRecovered', 'Confirmed', 'Deaths',
                                                     'Recovered'])
                                            ],
                                            value='NewConfirmed',
                                            clearable=False,
                                            className='linear-chart-dropdown-f'
                                        ),
                                        md=2
                                    )
                                ],
                                className='linear-chart-container-f'
                            )
                        ]
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
        Output('linear_chart_figure', 'figure'),
        Input('linear_chart_dropdown', 'value')
    )
    def update_linear_chart(target):

        return figure.linear_chart(country, target)

    app.run_server(debug=True)