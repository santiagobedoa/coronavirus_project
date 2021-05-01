import requests
import utils


class Data:

    def __init__(self):
        # AUTHORIZATION
        self.postman = {'Username': 'corona', 'Password': 'ZUav4vawzCfMcMXHV8B'}


    # GLOBAL INFORMATION
    def get_available_countries(self):
        '''
        Do a request to "https://api.covid19api.com/countries" and create a list with the
        available countries.
        Strucutre:
        [{'Country': str, 'Slug': str, 'ISO2': str}]
        :return: list of dict where each dict contains Country name, Slug name and ISO2 name that are available
        '''
        url = 'https://api.covid19api.com/countries'
        response = requests.request('GET', url, data=self.postman)
        json_raw_data = response.json()

        return json_raw_data


    def get_actual_global_data(self):
        '''
        Do a request to "https://api.covid19api.com/summary" and create a dictionary with
        the global data.
        Structure:
        {'NewConfirmed': int, 'TotalConfirmed': int, 'NewDeaths': int, 'TotalDeaths': int,
        'NewRecovered': int, 'TotalRecovered': int, 'Date': datetime.datetime(2021, 4, 4, 3, 19, 12, 662000)}
        :return: dict that contains the global data of the current day.
        '''
        url = 'https://api.covid19api.com/summary'
        response = requests.request('GET', url, data=self.postman)
        json_raw_data = response.json()
        global_data = utils.convert_date_to_time(json_raw_data['Global'])

        return global_data


    def get_all_countries_actual_data(self):
        '''
        Do a request to "https://api.covid19api.com/summary" and create a dictionary with
        the countries data.
        Structure:
        {'NewConfirmed': int, 'TotalConfirmed': int, 'NewDeaths': int, 'TotalDeaths': int,
        'NewRecovered': int, 'TotalRecovered': int, 'Date': datetime.datetime(2021, 4, 4, 3, 19, 12, 662000)}
        :return: dict that contains the global data of the current day.
        '''
        url = 'https://api.covid19api.com/summary'
        response = requests.request('GET', url, data=self.postman)
        json_raw_data = response.json()
        countries_data = json_raw_data['Countries']

        return countries_data


    # COUNTRY ACTUAL DATA
    def get_country_actual_data(self, country_name):
        '''
        Do a request to "https://api.covid19api.com/summary" and create a dictionary with
        the data of the desired country.
        Structure:
        {'ID': str, 'Country': str, 'CountryCode': str, 'Slug': str, 'NewConfirmed': int,
        'TotalConfirmed': int, 'NewDeaths': int, 'TotalDeaths': int, 'NewRecovered': int,
        'TotalRecovered': int, 'Date': datetime.datetime(2021, 4, 4, 3, 19, 12, 662000), 'Premium': {}}
        :param country_name: desired country to extract data.
        :return: dict that contains the data of the current day for the specified country.
        '''
        url = 'https://api.covid19api.com/summary'
        response = requests.request('GET', url, data=self.postman)
        json_raw_data = response.json()
        country_data = {}
        for country in json_raw_data['Countries']:
            if country['Country'].lower() == str(country_name):
                country_data = country

        data = utils.convert_date_to_time(country_data)

        return data


    # ALL DATA OF A COUNTRY
    def get_all_country_data(self, country_slug_name):
        '''
        Do a request to "https://api.covid19api.com/total/dayone/country/country_name"
        and create a list that contains dictionaries where each dictionary contains the information
        of one day. It goes from the first recorded case to the current day.
        Structure:
        {'Country': str, 'CountryCode': str, 'Province': str, 'City': str, 'CityCode': str,
         'Lat': str, 'Lon': str, 'Confirmed': int, 'Deaths': int, 'Recovered': int, 'Active': int,
         'Date': datetime.datetime(2021, 4, 2, 0, 0)}
        :param country_name: desired country in Slug form to extract data.
        :return: list wich contain dictionaries where each dict contain all cases by case type for a country from the first recorded case.
        '''
        url = f'https://api.covid19api.com/total/dayone/country/{country_slug_name}'
        response = requests.request('GET', url, data=self.postman)
        json_raw_data = response.json()
        if len(json_raw_data) == 0:
            return []
        # WARNING: in some cases json_raw_data contains "message" and "success" strings (they are not dicts).
        # I don't know why it happens. This is the reason why there is a condition in the list comprehension.
        data = [utils.convert_date_to_time(day_info) for day_info in json_raw_data if type(day_info) != str()]

        new_cases = False
        confirmed_day_before = 0
        deaths_day_before = 0
        recovered_day_before = 0
        for dictionary in data:

            if new_cases == False:
                dictionary['NewConfirmed'] = dictionary['Confirmed']
                dictionary['NewDeaths'] = dictionary['Deaths']
                dictionary['NewRecovered'] = dictionary['Recovered']
                confirmed_day_before = dictionary['Confirmed']
                deaths_day_before = dictionary['Deaths']
                recovered_day_before = dictionary['Recovered']
                new_cases = True

            else:
                new_confirmed = dictionary['Confirmed'] - confirmed_day_before
                new_deaths = dictionary['Deaths'] - deaths_day_before
                new_recovered = dictionary['Recovered'] - recovered_day_before

                if 0 < new_confirmed:
                    dictionary['NewConfirmed'] = new_confirmed
                else:
                    dictionary['NewConfirmed'] = 0

                if 0 < new_deaths:
                    dictionary['NewDeaths'] = new_deaths
                else:
                    dictionary['NewDeaths'] = 0

                if 0 < new_recovered:
                    dictionary['NewRecovered'] = new_recovered
                else:
                    dictionary['NewRecovered'] = 0

                confirmed_day_before = dictionary['Confirmed']
                deaths_day_before = dictionary['Deaths']
                recovered_day_before = dictionary['Recovered']
                new_cases = True

        return data