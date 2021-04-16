import requests
import ast
import support_functions
import pyttsx3
import speech_recognition
import os

class Data:
    def __init__(self):
        # AUTHORIZATION
        self.postman = {'Username':'corona','Password':'ZUav4vawzCfMcMXHV8B'}

    # GLOBAL INFORMATION
    def get_available_countries(self):
        '''
        Do a request to "https://api.covid19api.com/countries" and create a dictionary wth the
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
        str_raw_data = response.text
        raw_data = ast.literal_eval(str_raw_data)
        global_data = support_functions.convert_date_to_time(raw_data['Global'])

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
        response = requests.request('GET', url, data= self.postman)
        str_raw_data = response.text
        raw_data = ast.literal_eval(str_raw_data)
        countries_data = raw_data['Countries']

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
        str_raw_data = response.text
        raw_data = ast.literal_eval(str_raw_data)
        country_data = {}
        for country in raw_data['Countries']:
            if country['Country'].lower() == str(country_name):
                country_data = country

        data = support_functions.convert_date_to_time(country_data)

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
        str_raw_data = response.text
        raw_data = ast.literal_eval(str_raw_data)
        data = [support_functions.convert_date_to_time(day_info) for day_info in raw_data]
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


def open_global_visualization():
    cmd = os.path.join(os.getcwd(), "global_visualization.py")
    os.system('{} {}'.format('python', cmd))


def get_audio(language_input):
    '''
    Record and transcribe the recorded audio.
    :param language_input: language to be detected. "es" for spanish or "en" for english.
    :return: string that contains the audio recorded
    '''
    recognize = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = recognize.listen(source)
        text_said = str()

        if language_input.lower() == 'es':
            try:
                text_said = recognize.recognize_google(audio, language='es-CO')
            except Exception as e:
                print('Error in get_audio() function: '+str(e))

            return text_said.lower()

        else:
            try:
                text_said = recognize.recognize_google(audio, language='en-US')
            except Exception as e:
                print('Error in get_audio() function: ' + str(e))

            return text_said.lower()


def speak(text_to_speak):
    '''
    Speak the specified text
    :param text_to_speak: text to speak
    :return:
    '''
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) # speaker speed
    engine.say(text_to_speak)
    engine.runAndWait()


def main():
    data = Data()
    ola = data.get_all_country_data('colombia')
    print(ola)

#main()