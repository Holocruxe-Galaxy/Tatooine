#data_utils.py
import pymongo
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

from utils import debug_utils

class Data:
    def __init__(self,user_id) -> None:
        self.logger = debug_utils.logger
        self.predict = "food"
        self.user_id = user_id
    # MongoDB connection
    def mongodb_connection(self):
        try:
            client = pymongo.MongoClient("mongodb+srv://fierrof47:qR4didvGr1qWJ9YK@testcluster.m7ynzx9.mongodb.net/") #TODO modificarrrrrr
            database = client["holocheff_db"]
            return database
        except Exception as e:
            self.logger.error("An error occurred while connecting to MongoDB: " + str(e), extra={'color': '91'})
            self.logger.warn("The program is going to stop now...", extra={'color': '93'})

            exit()    
    
    # Import the data from MongoDB and convert it to a pandas DataFrame
    def get_meals(self):
        try:
            database = self.mongodb_connection()
            # Get meals data from data collection
            data = [item['meal'] for item in database["data"].find({}, {"meal": 1, "_id": 0})]
            # Convert MongoDB data to pandas DataFrame
            self.dataframe = pd.DataFrame(data)
            self.encoder = LabelEncoder()
            self.format()
            self.features,self.labels = self.features_labels_split()            
            self.features_train, self.features_eval, self.labels_train, self.labels_eval = self.train_test_split()  
            return self     
        except Exception as e:
            self.logger.error("An error occurred while getting the data: " + str(e), extra={'color': '91'})
            self.logger.warn("The program is going to stop now...", extra={'color': '93'})
         
    # Format the data with LabelEncoder
    def format(self):
        try:
            # Encode the categorical features
            weather_encoder = self.encoder
            self.dataframe['weather'] = weather_encoder.fit_transform(self.dataframe['weather'])
            
            location_encoder = self.encoder
            self.dataframe['location'] = location_encoder.fit_transform(self.dataframe['location'])
            
            food_encoder = self.encoder
            self.dataframe['food'] = food_encoder.fit_transform(self.dataframe['food'])

            # Add day of the week
            self.dataframe['day_of_week'] = pd.to_datetime(self.dataframe['date']).dt.dayofweek
            # Add hour of the day
            self.dataframe['hour_of_day'] = pd.to_datetime(self.dataframe['date']).dt.hour
            
            self.dataframe = self.dataframe.drop(columns=['date'])            

        except Exception as e:
            # Log the error and inform the program is going to stop
            self.logger.error("An error occurred while formatting the data: " + str(e), extra={'color': '91'})
            self.logger.warn("The program is going to stop now...", extra={'color': '93'})
            exit()
   
    # Get the features from the dataset and drop the predict columns
    def features_labels_split(self):
        try:
            features = np.array(self.dataframe.drop(self.predict, axis=1))
            labels = np.array(self.dataframe[self.predict])
            return features, labels
        except Exception as e:
            self.logger.error(f"Error occurred while getting features and labels: {e}", extra={'color': '91'})
            return None, None

    # Split the data into training and evaluation sets
    def train_test_split(self, test_size=0.3):
        try:
            return train_test_split(self.features, self.labels, test_size=test_size)
        except Exception as e:
            self.logger.error(f"Error occurred while splitting the data: {e}", extra={'color': '91'})
            return None, None, None, None
