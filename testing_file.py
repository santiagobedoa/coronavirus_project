import pymongo
from connect_to_api import Data
import ssl


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


    def check(self):
        collection = self.database['colombia']
        result = [x for x in collection.find()]
        new_collection = self.database['aaaa-prueba']
        new_collection.insert_one(result[1])


if __name__ == '__main__':
    db = READ_DATABASE()
    db.check()