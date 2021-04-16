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

country = 'Colombia'

def create_country_active_cases_card(desired_country):
    desired_country = str(desired_country)
    data = Data()
    available_countries = data.get_available_countries()
    slug_country_name = str()
    for country_dict in available_countries:
        if country_dict['Country'].lower() == desired_country.lower():
            slug_country_name = country_dict['Slug']

    data = data.get_all_country_data(slug_country_name)
    last_report = data[-1]
    active_cases = last_report['Active']

    card_figure = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H1(str(country), className='header-global-title'),
                    html.P('Active Cases:', className='header-number-description'),
                    html.P(f'{active_cases:,}', className='header-big-number-style')
                ]
            )
        ],
        className='card-header-item'
    )

    return card_figure


def create_card(desired_country, target):
    desired_country = str(desired_country)
    target = str(target)
    data = Data()
    available_countries = data.get_available_countries()
    slug_country_name = str()
    for country_dict in available_countries:
        if country_dict['Country'].lower() == desired_country.lower():
            slug_country_name = country_dict['Slug']

    country_summary = data.get_country_actual_data(slug_country_name)

    big_number_value = country_summary['Total'+target]
    new_cases_value = country_summary['New'+target]

    card_figure = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H6(children=target, className='card-title-style'),
                    html.P(f'{big_number_value:,}', className='card-big-number-style'),
                    html.P(f'New Cases: {new_cases_value:,}', className='card-new-cases-style')
                ]
            )
        ],
        className='card-item'
    )

    return card_figure


def create_line_chart(desired_country, target):
    target = str(target)
    data = Data()

    available_countries = data.get_available_countries()
    slug_country_name = str()
    for country_dict in available_countries:
        if country_dict['Country'].lower() == desired_country.lower():
            slug_country_name = country_dict['Slug']

    country_data = data.get_all_country_data(slug_country_name)
    df = pd.DataFrame(country_data)

    line_chart_figure = go.Figure()
    line_chart_figure.add_trace(go.Scatter(x=df['Date'], y=df[target],
                                           mode='lines', connectgaps=True,
                                           name=target))

    line_chart_figure.update_layout(
        title=dict(
            text=str(target),
            font_family='sans-serif',
            font_size=30,
            font_color='#F39C12',
            xanchor='center',
            x=0.5
        ),
        xaxis_title='Date',
        yaxis_title='Number of Cases',
        legend_title='Country',
        paper_bgcolor="#4E5D6C",
        font_color='#CFCFCF'
    )

    return line_chart_figure


app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])

app.layout = html.Div(
    [
        html.Div(
            [
                html.P('🦠', className='header-emoji'),
                html.H1('Coronavirus Tracker', className='header-title'),
                html.P(
                    'In this section you will find a series of visualizations describing the evolution of the coronavirus.',
                    className='header-description')
            ],
            className='header-container',
        ),
        dbc.Container(
            [
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(create_country_active_cases_card(country), md=12)
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(create_card(country, 'Confirmed'), md=4),
                                dbc.Col(create_card(country, 'Deaths'), md=4),
                                dbc.Col(create_card(country, 'Recovered'), md=4),
                            ]
                        )
                    ],
                    className='cards-container'
                ),
                dbc.Container(
                    [
                        html.H1('Linear Charts', className='charts-title'),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(id='new_cases_chart', figure=create_line_chart(country, 'NewDeaths')),
                                    md=10
                                ),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id='new_cases_dropdown',
                                        options=[
                                            {'label': concept, 'value': concept}
                                            for concept in ['NewConfirmed', 'NewDeaths', 'NewRecovered']
                                        ],
                                        value='NewConfirmed',
                                        clearable=False,
                                        className='charts_dropdown'
                                    ),
                                    md=2
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(id='total_cases_chart', figure=create_line_chart(country, 'Confirmed')),
                                    md=10
                                ),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id='total_cases_dropdown',
                                        options=[
                                            {'label': concept, 'value': concept}
                                            for concept in ['Confirmed', 'Deaths', 'Recovered']
                                        ],
                                        value='Confirmed',
                                        clearable=False,
                                        className='charts_dropdown'
                                    ),
                                    md=2
                                )
                            ]
                        )
                    ],
                    className='charts-container'
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
    Output('total_cases_chart', 'figure'),
    Input('total_cases_dropdown', 'value')
)
def update_total_cases(concept):
    figure = create_line_chart(country, str(concept))

    return figure


@app.callback(
    Output('new_cases_chart', 'figure'),
    Input('new_cases_dropdown', 'value')
)
def update_new_cases(concept):
    figure = create_line_chart(country, str(concept))

    return figure

app.run_server(debug=True)
