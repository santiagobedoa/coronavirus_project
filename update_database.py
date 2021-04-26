import pymongo
from main import Data
import ssl

class UPDATE_DATABASE:

    def __init__(self):
        self.password = 'Coronavirus_project_BEDO'
        self.db_name = 'Coronavirus_project_DB'
        self.data = Data()
        self.client = pymongo.MongoClient(
            f"mongodb+srv://santiagobedoa:{self.password}@coronaviruscluster.ugpmg.mongodb.net/{self.db_name}?retryWrites=true&w=majority",
            ssl=True,
            ssl_cert_reqs=ssl.CERT_NONE)
        self.database = self.client['Coronavirus_project_DB']


    def update_global_data(self):
        '''
        Updates the "global_data" data that is stored in the database
        :return:
        '''
        self.database.global_data.drop()
        collection = self.database['global_data']
        collection.insert_one((self.data.get_actual_global_data()))

        print('Done! global_data updated...')


    def update_available_countries(self):
        '''
        Updates the "available_countries" data that is stored in the database
        :return:
        '''
        self.database.available_countries.drop()
        collection = self.database['available_countries']
        collection.insert_many(self.data.get_available_countries())

        print('Done! available_countries updated...')


    def update_countries_actual_data(self):
        '''
        Updates the "countries_actual_data" data that is stored in the database
        :return:
        '''
        self.database.countries_actual_data.drop()
        collection = self.database['countries_actual_data']
        collection.insert_many(self.data.get_all_countries_actual_data())

        print('Done! countries_actual_data updated...')


    def update_countries_historical_data(self):
        '''
        Updates the "acountries_historical_data" data that is stored in the database
        :return:
        '''
        collections = self.database.list_collection_names()
        available_countries = [country['Slug'] for country in self.database['available_countries'].find()]
        for count, country in enumerate(available_countries):
            print(f'{str(count+1)}: {country}')
            all_data = self.data.get_all_country_data(country)

            if 0 < len(all_data):
                collection = self.database[country]

                if country in collections:
                    last_recorded_date = [x['Date'] for x in self.database[country].find()][-1]
                    if all_data[-2]['Date'] == last_recorded_date:
                        last_data = all_data[-1]
                        collection.insert_one(last_data)
                    else:
                        self.database.drop[country]
                        collection = self.database[country]
                        collection.insert_many(all_data)
                else:
                    self.database.drop[country]
                    collection = self.database[country]
                    collection.insert_many(all_data)

            else:
                print(f'--- No available information for {country} ---')

        print('Done! all available historical data updated...')
