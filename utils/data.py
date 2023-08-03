import pymongo
import pandas as pd
from pymongo import MongoClient
from sklearn.preprocessing import LabelEncoder

from utils import debug as debug_utils

logger = debug_utils.logger

def mongodb_connection():
    client = pymongo.MongoClient("mongodb+srv://fierrof47:qR4didvGr1qWJ9YK@testcluster.m7ynzx9.mongodb.net/")
    db = client["holocheff_db"]
    return db

# Import the data from MongoDB and convert it to a pandas DataFrame
def get_data():
    try:
        logger.debug("Getting data...", extra={'color': '93'})
        # Connect to MongoDB
   
        database = mongodb_connection()
        # Get meals data from data collection
        data = database["data"].find({}, {"meal": 1, "_id": 0})
        
        # Convert MongoDB data to pandas DataFrame
        dataframe = pd.DataFrame(list(data))

        logger.info("Data successfully retrieved!", extra={'color': '92'})
        return dataframe
    except Exception as e:
        logger.error("An error occurred while getting the data: " + str(e), extra={'color': '91'})
        logger.debug("The program is going to stop now...", extra={'color': '91'})
        exit()

# Format the data
def format_data(dataframe):
    try:
        logger.debug("Formatting data...", extra={'color': '93'})
        # Remove the _id column
        dataframe = dataframe.drop(columns=['_id','user_id'])

        label_encoder = LabelEncoder()

        # Encode the categorical features
        dataframe['weather'] = label_encoder.fit_transform(dataframe['weather'])
        dataframe['location'] = label_encoder.fit_transform(dataframe['location'])
        dataframe['food_id'] = label_encoder.fit_transform(dataframe['food_id'])

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
        
