import pymongo
from connect_to_api import Data
import ssl
import pandas as pd

class READ_DATABASE:

    def __init__(self):
        self.password = 'Coronavirus_project_BEDO'
        self.db_name = 'Coronavirus_project_DB'
        self.data = Data()
        self.client = pymongo.MongoClient(
            f"mongodb+srv://santiagobedoa:{self.password}@coronaviruscluster.ugpmg.mongodb.net/{self.db_name}?retryWrites=true&w=majority",
            ssl=True,
            ssl_cert_reqs=ssl.CERT_NONE)
        self.database = self.client['Coronavirus_project_DB']


    def global_status_data(self):
        '''
        Connect to the database where the data is stored and read "global_status_data" collection.
        :return: dict with the global status information
        '''
        collection = self.database['global_data']

        return collection.find_one()


    def df_countries_status(self):
        '''
        Connect to the database where the data is stored and read "global_status_data" collection.
        :return: dataframe with the current status of a countries.
        '''
        collection = self.database['countries_status']
        result = list(collection.find())

        return pd.DataFrame(result)


    def country_historical_data(self, country):
        '''
        Connect to the database where the data is stored and read "global_status_data" collection.
        :return: list of dicts where each dict contains the status of a specific date.
        '''
        collection = self.database[country.lower()]
        result = list(collection.find())

        return result



if __name__ == '__main__':
    db = READ_DATABASE()
    print(db.country_historical_data('Colombia')[-1]['Active'])

