
import pandas as pd
from pymongo import MongoClient


# Traer los datos de la base de datos y crear un dataframe .csv
def import_data():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    database = client['holocheff_db_test']
    collection = database['meals']

    # Query the data from MongoDB
    data = collection.find({})  # You can customize the query as per your requirements

    # Convert MongoDB data to pandas DataFrame
    df = pd.DataFrame(list(data))

    # Convert DataFrame to CSV
    df.to_csv('data/dataframe.csv', index=False)

# Formateamos el dataframe para poder utilizarlo en el modelo
def format_data():
    pass



