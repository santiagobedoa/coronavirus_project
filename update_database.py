import pymongo
from connect_to_api import Data
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


    def update_countries_status(self):
        '''
        Updates the "countries_actual_data" data that is stored in the database
        :return:
        '''
        self.database.countries_status.drop()
        collection = self.database['countries_status']
        collection.insert_many(self.data.get_all_countries_actual_data())

        print('Done! countries_actual_data updated...')


    def update_countries_historical_data(self):
        '''
        Updates the "countries_historical_data" data that is stored in the database
        :return:
        '''
        available_countries = [country['Slug'] for country in self.database['available_countries'].find()]
        for count, country in enumerate(available_countries):
            print(f'{str(count+1)}: {country}')
            all_data = self.data.get_all_country_data(country)

            if 0 < len(all_data):
                self.database.drop[country]
                collection = self.database[country]
                collection.insert_many(all_data)

            else:
                print(f'--- No available information for {country} ---')

        print('Done! all available historical data updated...')


if __name__ == '__main__':

    db = UPDATE_DATABASE()
    db.update_global_data()
    db.update_available_countries()
    db.update_countries_status()
    db.update_countries_historical_data()