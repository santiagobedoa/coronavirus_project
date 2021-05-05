from dash import Dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from graphs import FIGURE
from read_database import READ_DATABASE


if __name__ == '__main__':

    figure = FIGURE()
    read_database = READ_DATABASE()

    # Initialize Dash app
    app = Dash(external_stylesheets=[dbc.themes.SUPERHERO])
    server = app.server

    # Set app layout
    app.layout = html.Div(
        [
            # --- HEADER ---
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
                    # --- GLOBAL INFORMATION CARDS ---
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
                    # --- MAP ---
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
                            dbc.Row(
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
                    # --- COUNTRIES SECTION ---
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    html.H1('Country Visualization', className='country-visualization-title-f'),
                                    html.P('Search Country:', className='country-search-text-f'),
                                    dcc.Dropdown(
                                        id='countries-dropdown-id',
                                        options=[
                                            {'label': target, 'value': target} for target in
                                            list(read_database.df_available_countries()['Slug'])
                                        ],
                                        value='colombia',
                                        clearable=False,
                                        className='countries-dropdown-f'
                                    ),
                                ]
                            )
                        ]
                    ),
                    # --- COUNTRY INFORMATION CARDS ---
                    html.Div(id='country-cards-section-id'),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    dcc.Dropdown(
                                        id='linear_chart_dropdown_id',
                                        options=[
                                            {'label': target, 'value': target}
                                            for target in (
                                                ['NewConfirmed', 'NewDeaths', 'NewRecovered', 'Confirmed', 'Deaths',
                                                 'Recovered'])
                                        ],
                                        value='NewConfirmed',
                                        clearable=False,
                                        className='countries-dropdown-f'
                                    ),
                                ]
                            )
                        ]
                    ),
                    # --- COUNTRY LINE CHART ---
                    html.Div(id='line-chart-section-id'),
                    # --- BAR CHART ---
                    dbc.Container(
                        [
                            html.H6('Most Affected Countries', className='graph-title-f'),
                            dcc.Dropdown(
                                id='bar_chart_dropdown_id',
                                options=[
                                    {'label': target, 'value': target} for target in [
                                        'TotalConfirmed', 'TotalDeaths', 'TotalRecovered',
                                        'NewConfirmed', 'NewDeaths', 'NewRecovered'
                                    ]
                                ],
                                value='TotalConfirmed',
                                clearable=False,
                                className='bar-chart-dropdown-f'
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(dcc.Graph(id='bar_chart_id' , figure=figure.bar_chart()))
                                ],
                                className='bar-chart-f',
                                align='center'
                            )
                        ]
                    ),
                    # --- CREDITS ---
                    dbc.Container(
                        [
                            html.P('Made in Colombia...', className='credits-text-f'),
                            html.P('By Bedo', className='credits-text-f')
                        ],
                        className='credits-container-f'
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


    @app.callback(
        Output('country-cards-section-id', 'children'),
        Input('countries-dropdown-id', 'value')
    )
    def update_country_cards(country):
        html_visualization = dbc.Container(
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
        )
        return html_visualization


    @app.callback(
        Output('line-chart-section-id', 'children'),
        Input('countries-dropdown-id', 'value'),
        Input('linear_chart_dropdown_id', 'value')
    )
    def update_county_line_chart(country, target):
        html_linechart = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(
                                id='linear_chart_figure',
                                figure=figure.linear_chart(country, target)
                            ),
                            md=12
                        )
                    ],
                    className='linear-chart-container-f'
                )
            ]
        )
        return html_linechart


    @app.callback(
        Output('bar_chart_id', 'figure'),
        Input('bar_chart_dropdown_id', 'value')
    )
    def update_bar_chart(target):
        return figure.bar_chart(target)


    app.run_server(debug=True)