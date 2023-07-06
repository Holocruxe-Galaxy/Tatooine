
import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Traer los datos de la base de datos y crear un dataframe .csv


def import_data():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    database = client['holocheff_db_test']
    collection = database['meals']

    # Query the data from MongoDB
    # You can customize the query as per your requirements
    data = collection.find({})

    # Convert MongoDB data to pandas DataFrame
    dataframe = pd.DataFrame(list(data))

    # Convert DataFrame to CSV
    dataframe.to_csv('data/dataframe.csv', index=False)


def get_dataframe():
    dataframe = pd.read_csv('data/dataframe.csv')
    return dataframe

# Formateamos el dataframe para poder utilizarlo en el modelo


def format_data():
   # Encode the categorical features
    dataframe = get_dataframe()
    label_encoder = LabelEncoder()
    dataframe['breakfast'] = label_encoder.fit_transform(
        dataframe['breakfast'])
    dataframe['lunch'] = label_encoder.fit_transform(dataframe['lunch'])
    dataframe['dinner'] = label_encoder.fit_transform(dataframe['dinner'])
    dataframe.to_csv('data/dataframe.csv', index=False)


# funcion para devolver el dataframe de entrenamiento
def get_training_data():
    dataframe = get_dataframe()
    train_data, _ = train_test_split(
        dataframe, train_size=0.7, random_state=42)
    return train_data


# funcion para devolver el dataframe de testeo
def get_testing_data():
    dataframe = get_dataframe()
    _, test_data = train_test_split(dataframe, test_size=0.3, random_state=42)
    return test_data
