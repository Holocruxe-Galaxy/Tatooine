#data_utils.py
import pymongo
import pandas as pd
import numpy as np
import sklearn
import json
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split


class Data:
    def __init__(self,user_id) -> None:
        self.predict = "food"
        self.user_id = user_id
    # MongoDB connection
    def mongodb_connection(self):
        try:
            client = pymongo.MongoClient("mongodb+srv://fierrof47:qR4didvGr1qWJ9YK@testcluster.m7ynzx9.mongodb.net/") #TODO modificarrrrrr
            database = client["holocheff_db"]
            return database
        except Exception as e:
            print("An error occurred: " + str(e))
            exit()    
    
    # Import the data from MongoDB and convert it to a pandas DataFrame
    def get_meals(self):
        try:
            database = self.mongodb_connection()
            # Get meals data from data collection
            all_data = list(database["data"].find({}))
            
            # Extracting meals from all data items
            meals_list = []
            for item in all_data:
                meals_list.extend(item['meals'])
                        # Convert MongoDB meals data to pandas DataFrame
            self.dataframe = pd.DataFrame(meals_list)         

            # Set the encoder
            self.encoder = LabelEncoder()
            # Format the data
            self.format()
            # Split the data into features and labels and then into training and evaluation sets 
            self.features, self.labels = self.features_labels_split()            
            self.features_train, self.features_eval, self.labels_train, self.labels_eval = self.train_test_split()  
            return self     
            
        except Exception as e:
            print("An error occurred: " + str(e))

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
            print("An error occurred: " + str(e))
            exit()
   
    # Get the features from the dataset and drop the predict columns
    def features_labels_split(self):
        try:
            features = np.array(self.dataframe.drop(self.predict, axis=1))
            labels = np.array(self.dataframe[self.predict])
            return features, labels
        except Exception as e:
            print("An error occurred: " + str(e))
            return None, None

    # Split the data into training and evaluation sets
    def train_test_split(self, test_size=0.3):
        try:
            return train_test_split(self.features, self.labels, test_size=test_size)
        except Exception as e:
            print("An error occurred: " + str(e))
            return None, None, None, None

    # Insert input data into the database
    def insert_input(self, input_data):
        try:
            # Insert the input data into the database
            self.database["data"].insert_one(input_data)
        except Exception as e:
            print("An error occurred: " + str(e))

    # Load the data format from the JSON file
    def load_data_format(self):
        try:
            with open('data_format.json', 'r') as f:
                data_format = json.load(f)
            return data_format
        except Exception as e:
            print("An error occurred: " + str(e))
            return None
    
    # Validate the input data format
    def input_validate_format(self, input_data):
        try:
            # Check if the input data matches the data format
            if input_data.keys() != self.data_format.keys():                
                return False
            
            for key in self.data_format.keys():
                if isinstance(self.data_format[key], dict):
                    if input_data[key].keys() != self.data_format[key].keys():
                        
                        return False
                    for sub_key in self.data_format[key].keys():
                        if not isinstance(input_data[key][sub_key], type(self.data_format[key][sub_key])):                            
                            return False
                else:
                    if not isinstance(input_data[key], type(self.data_format[key])):                        
                        return False            
            return True
        except Exception as e:
            print("An error occurred: " + str(e))
            return False