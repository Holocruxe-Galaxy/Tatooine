
import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Import the data from MongoDB and save it as a CSV file
def get_dataframe():
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        database = client['holocheff_db_test']
        collection = database['meals']

        # Query the data from MongoDB
        data = collection.find({})

        # Convert MongoDB data to pandas DataFrame
        dataframe = pd.DataFrame(list(data))

        ################Por que no funciona dentro de format_data()
        dataframe = dataframe.drop(['_id'], axis=1)
        dataframe = dataframe.drop(['user_id'], axis=1)
        # Convert date to day of the week
        dataframe['date'] = pd.to_datetime(dataframe['date']).dt.dayofweek

        # Format the data
        format_data(dataframe)
        return dataframe
    except Exception as e:
        print("An error occurred while retrieving the data:", str(e))


# Format the data and save it as a CSV file
def format_data(dataframe):
    try:
        # Get the data from the CSV file
        label_encoder = LabelEncoder()

        # Encode the categorical features
        dataframe['breakfast'] = label_encoder.fit_transform(dataframe['breakfast'])
        dataframe['lunch'] = label_encoder.fit_transform(dataframe['lunch'])
        dataframe['dinner'] = label_encoder.fit_transform(dataframe['dinner'])

        # ################ no funciona-------------
        # dataframe = dataframe.drop(['_id'], axis=1)
        # dataframe = dataframe.drop(['user_id'], axis=1)
     




        print("Data formatted.")     
    except Exception as e:
        print("An error occurred during data formatting:", str(e))

# Convert the dataframe to a CSV file for testing
def convert_to_csv():
    try:
        # Get the data from the CSV file
        dataframe = get_dataframe()
        # Save the data as a CSV file
        dataframe.to_csv('data/dataframe.csv', index=False)
        print("Data saved for testing in dataframe.csv.")
    except Exception as e:
        print("An error occurred while converting the data to a CSV file:", str(e))


# Get the training and eval data from the DataFrame as a tuple
def get_training_data():
    try:
        dataframe = get_dataframe()
        # Split the data into training and eval sets
        training_set, eval_set = train_test_split(dataframe, test_size=0.2, random_state=0)
        # Convert the data into a tuple
        training_tuple = (training_set, eval_set)
        return training_tuple
    except Exception as e:
        print("An error occurred while retrieving the training data:", str(e))
        return None
