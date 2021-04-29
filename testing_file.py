import pymongo
import ssl
import pandas as pd

from connect_to_api import Data

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


    def read_global_status(self):
        collection = self.database['global_data']

        return collection.find_one()


    def df_countries_status(self):
        collection = self.database['countries_actual_data']
        result = list(collection.find())

        return pd.DataFrame(result)


    def check(self):
        collection = self.database['colombia']
        # print(list(collection.find())[-1])
        #
        # connect_to_api = Data()
        # print(list(connect_to_api.get_all_country_data('colombia'))[-1])
        print(collection.find_one().sort('_id',-1))




if __name__ == '__main__':

    db = READ_DATABASE()
    db.check()
