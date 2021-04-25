import pymongo
from main import Data
import ssl

class UPDATE_DATABASE:

    def __init__(self):
        self.password = 'Mascota0312'
        self.db_name = 'Coronavirus_project_DB'
        self.data = Data()
        self.client = pymongo.MongoClient(
            f"mongodb+srv://santiagobedoa:{self.password}@coronaviruscluster.ugpmg.mongodb.net/{self.db_name}?retryWrites=true&w=majority",
            ssl=True,
            ssl_cert_reqs=ssl.CERT_NONE)
        self.database = self.client['Coronavirus_project_DB']


    def update_global_data(self):
        self.database.global_data.drop()
        collection = self.database['global_data']
        collection.insert_one((self.data.get_actual_global_data()))


    def update_available_countries(self):
        self.database.available_countries.drop()
        collection = self.database['available_countries']
        for country in self.data.get_available_countries():
            collection.insert_one(country)




def main():
    db = UPDATE_DATABASE()
    db.update_available_countries()

main()

