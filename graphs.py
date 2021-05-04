import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
from read_database import READ_DATABASE
import pandas as pd

class FIGURE:

    def __init__(self):
        self.db = READ_DATABASE()


    def global_status_card(self, target):
        big_number = self.db.global_status_data()[f'Total{target}']
        new_cases_number = self.db.global_status_data()[f'New{target}']

        card_figure = dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H6(target, className='card-title-f'),
                        html.P(f'{big_number:,}', className='card-big-number-f'),
                        html.P(f'New Cases: {new_cases_number:,}', className='card-new-cases-f')
                    ],
                    className='card-content'
                )
            ],
            className='card-figure-f'
        )

        return card_figure


    def country_status_card(self, country, target):
        big_number = self.db.country_historical_data(country)[-1][target]
        new_cases_number = self.db.country_historical_data(country)[-1][f'New{target}']

        card_figure = dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H1(target, className='card-title-f'),
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


    def linear_chart(self, country, target):
        df = pd.DataFrame(self.db.country_historical_data(country))
        df.drop_duplicates('Date', keep='first', inplace=True)
        linear_chart_figure = go.Figure()
        linear_chart_figure.add_trace(
            go.Scatter(
                x=df['Date'],
                y=df[target],
                mode='lines',
                connectgaps=True,
                name=target
            )
        )
        linear_chart_figure.update_layout(
            title=dict(
                text=target,
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

        return linear_chart_figure


