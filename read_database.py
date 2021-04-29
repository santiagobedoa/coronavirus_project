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


    def read_global_status(self):
        collection = self.database['global_data']

        return collection.find_one()


    def df_countries_status(self):
        collection = self.database['countries_actual_data']
        result = list(collection.find())

        return pd.DataFrame(result)
