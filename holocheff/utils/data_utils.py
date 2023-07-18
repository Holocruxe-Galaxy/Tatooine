import pandas as pd
import tensorflow as tf
import pymongo
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# Import the data from MongoDB and convert it to a pandas DataFrame
def get_data():
    try:
        print("\033[93m" + "Getting the data..." + "\033[0m")
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        database = client['holocheff_db']
        collection = database['meals']

        # Query the data from MongoDB
        data = collection.find({})

        # Convert MongoDB data to pandas DataFrame
        dataframe = pd.DataFrame(list(data))

        print("\033[92m" + "Data successfully retrieved!" + "\033[0m")
        return dataframe
    except Exception as e:
        print("\033[91m" + "An error occurred while getting the data:", str(e) + "\033[0m")
        return None

# Format the data
def format_data(dataframe):
    try:
        print("\033[93m" + "Formatting the data..." + "\033[0m")
        # Remove the _id column
        dataframe = dataframe.drop(columns=['_id','user_id'])

        label_encoder = LabelEncoder()

        # Encode the categorical features
        dataframe['weather'] = label_encoder.fit_transform(dataframe['weather'])
        dataframe['location'] = label_encoder.fit_transform(dataframe['location'])
        dataframe['breakfast'] = label_encoder.fit_transform(dataframe['breakfast'])
        dataframe['lunch'] = label_encoder.fit_transform(dataframe['lunch'])
        dataframe['dinner'] = label_encoder.fit_transform(dataframe['dinner'])

        # Add day of the week
        dataframe['day_of_week'] = pd.to_datetime(dataframe['date']).dt.dayofweek
        dataframe = dataframe.drop(columns=['date'])
        print("\033[92m" + "Data successfully formatted!" + "\033[0m")
        return dataframe

    except Exception as e:
        print("\033[91m" + "An error occurred while formatting the data:", str(e) + "\033[0m")
        return None

def get_users():
    pass