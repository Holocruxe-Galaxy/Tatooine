#data_utils.py
import pymongo
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from utils import debug_utils

logger = debug_utils.logger

def mongodb_connection():
    client = pymongo.MongoClient("mongodb+srv://fierrof47:qR4didvGr1qWJ9YK@testcluster.m7ynzx9.mongodb.net/")
    database = client["holocheff_db"]
    return database

# Import the data from MongoDB and convert it to a pandas DataFrame
def get_data():
    try:
        logger.debug("Getting data...", extra={'color': '93'})
        # Connect to MongoDB
   
        database = mongodb_connection()
        # Get meals data from data collection
        data = [item['meal'] for item in database["data"].find({}, {"meal": 1, "_id": 0})]
        # Convert MongoDB data to pandas DataFrame
        dataframe = pd.DataFrame(data)
       

        logger.info("Data successfully retrieved!", extra={'color': '92'})
        return dataframe
    except Exception as e:
        logger.error("An error occurred while getting the data: " + str(e), extra={'color': '91'})
        logger.debug("The program is going to stop now...", extra={'color': '91'})
        exit()

# Format the data
def format_data_LabelEncoder(dataframe):
    try:
        logger.debug("Formatting data...", extra={'color': '93'})

        # Encode the categorical features
        weather_encoder = LabelEncoder()
        dataframe['weather'] = weather_encoder.fit_transform(dataframe['weather'])
        
        location_encoder = LabelEncoder()
        dataframe['location'] = location_encoder.fit_transform(dataframe['location'])
        
        food_encoder = LabelEncoder()
        dataframe['food'] = food_encoder.fit_transform(dataframe['food'])

        # Add day of the week
        dataframe['day_of_week'] = pd.to_datetime(dataframe['date']).dt.dayofweek
        # Add hour of the day
        dataframe['hour_of_day'] = pd.to_datetime(dataframe['date']).dt.hour
        
        dataframe = dataframe.drop(columns=['date'])

        logger.info("Data successfully formatted!", extra={'color': '92'})
        return dataframe

    except Exception as e:
        # Log the error and inform the program is going to stop
        logger.error("An error occurred while formatting the data: " + str(e), extra={'color': '91'})
        logger.debug("The program is going to stop now...", extra={'color': '91'})
        exit()



def format_data_OneHotEncoder(dataframe):
    try:
        logger.debug("Formatting data...", extra={'color': '93'})

        # Identify categorical columns
        categorical_columns = ['weather', 'location']

        # Apply One-Hot Encoding
        encoder = OneHotEncoder()
        categorical_data = encoder.fit_transform(dataframe[categorical_columns]).toarray()
        categorical_feature_names = encoder.get_feature_names_out(categorical_columns)
        categorical_dataframe = pd.DataFrame(categorical_data, columns=categorical_feature_names)

        # Drop the original categorical columns from the DataFrame
        dataframe = dataframe.drop(columns=categorical_columns)

        # Add day of the week and hour of the day
        dataframe['day_of_week'] = pd.to_datetime(dataframe['date']).dt.dayofweek
        dataframe['hour_of_day'] = pd.to_datetime(dataframe['date']).dt.hour
        dataframe = dataframe.drop(columns=['date'])

        # Concatenate one-hot encoded columns with numerical features
        dataframe = pd.concat([dataframe, categorical_dataframe], axis=1)

        logger.info("Data successfully formatted!", extra={'color': '92'})
        return dataframe

    except Exception as e:
        # Log the error and inform the program is going to stop
        logger.error("An error occurred while formatting the data: " + str(e), extra={'color': '91'})
        logger.debug("The program is going to stop now...", extra={'color': '91'})
        exit()
