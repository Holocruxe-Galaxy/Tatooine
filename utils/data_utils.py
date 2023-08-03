#data_utils.py
import pymongo
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from utils import debug_utils



class Data:
    def __init__(self, encoder) -> None:
        self.logger = debug_utils.logger
        self.get_data()
        if encoder == "one_hot_encoder":
            self.format_data_OneHotEncoder()
        elif encoder == "label_encoder":
            self.format_data_LabelEncoder()

    @staticmethod
    def mongodb_connection():
        client = pymongo.MongoClient("mongodb+srv://fierrof47:qR4didvGr1qWJ9YK@testcluster.m7ynzx9.mongodb.net/")
        database = client["holocheff_db"]
        return database


    # Import the data from MongoDB and convert it to a pandas DataFrame
    def get_data(self):
        try:
            self.logger.debug("Getting data...", extra={'color': '93'})
            # Connect to MongoDB
    
            database = self.mongodb_connection()
            # Get meals data from data collection
            data = [item['meal'] for item in database["data"].find({}, {"meal": 1, "_id": 0})]
            # Convert MongoDB data to pandas DataFrame
            self.dataframe = pd.DataFrame(data)
       

            self.logger.info("Data successfully retrieved!", extra={'color': '92'})
            return self.dataframe
        except Exception as e:
            self.logger.error("An error occurred while getting the data: " + str(e), extra={'color': '91'})
            self.logger.debug("The program is going to stop now...", extra={'color': '91'})
            exit()

    # Format the data
    def format_data_LabelEncoder(self):
        try:
            self.logger.debug("Formatting data with LabelEncoder...", extra={'color': '93'})

            # Encode the categorical features
            weather_encoder = LabelEncoder()
            self.dataframe['weather'] = weather_encoder.fit_transform(self.dataframe['weather'])
            
            location_encoder = LabelEncoder()
            self.dataframe['location'] = location_encoder.fit_transform(self.dataframe['location'])
            
            food_encoder = LabelEncoder()
            self.dataframe['food'] = food_encoder.fit_transform(self.dataframe['food'])

            # Add day of the week
            self.dataframe['day_of_week'] = pd.to_datetime(self.dataframe['date']).dt.dayofweek
            # Add hour of the day
            self.dataframe['hour_of_day'] = pd.to_datetime(self.dataframe['date']).dt.hour
            
            self.dataframe = self.dataframe.drop(columns=['date'])

            self.logger.info("Data successfully formatted!", extra={'color': '92'})
            return self.dataframe

        except Exception as e:
            # Log the error and inform the program is going to stop
            self.logger.error("An error occurred while formatting the data: " + str(e), extra={'color': '91'})
            self.logger.debug("The program is going to stop now...", extra={'color': '91'})
            exit()



    def format_data_OneHotEncoder(self):
        try:
            self.logger.debug("Formatting data using OneHotEncoder...", extra={'color': '93'})

            # Identify categorical columns
            categorical_columns = ['weather', 'location']

            # Apply One-Hot Encoding
            encoder = OneHotEncoder()
            categorical_data = encoder.fit_transform(dataframe[categorical_columns]).toarray()
            categorical_feature_names = encoder.get_feature_names_out(categorical_columns)
            categorical_dataframe = pd.DataFrame(categorical_data, columns=categorical_feature_names)

            # Drop the original categorical columns from the DataFrame
            self.dataframe = self.dataframe.drop(columns=categorical_columns)

            # Add day of the week and hour of the day
            dataframe['day_of_week'] = pd.to_datetime(dataframe['date']).dt.dayofweek
            dataframe['hour_of_day'] = pd.to_datetime(dataframe['date']).dt.hour
            dataframe = dataframe.drop(columns=['date'])

            # Concatenate one-hot encoded columns with numerical features
            self.dataframe = pd.concat([dataframe, categorical_dataframe], axis=1)

            self.logger.info("Data successfully formatted!", extra={'color': '92'})
            return dataframe

        except Exception as e:
            # Log the error and inform the program is going to stop
            self.logger.error("An error occurred while formatting the data: " + str(e), extra={'color': '91'})
            self.logger.debug("The program is going to stop now...", extra={'color': '91'})
            exit()

