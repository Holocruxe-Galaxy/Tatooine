import pandas as pd
import tensorflow as tf
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# Import the data from MongoDB and convert it to a pandas DataFrame
def get_dataframe():
    try:
        print("\033[93m" + "Getting the data..." + "\033[0m")
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        database = client['holocheff_db_test']
        collection = database['meals']

        # Query the data from MongoDB
        data = collection.find({})

        # Convert MongoDB data to pandas DataFrame
        dataframe = pd.DataFrame(list(data))

        # Format the data
        dataframe = format_data(dataframe)
        
        print("\033[92m" + "Data successfully retrieved!" + "\033[0m")
        return dataframe
    except Exception as e:
        print("\033[91m" + "An error occurred while getting the data:", str(e) + "\033[0m")
        return None

# Format the data
def format_data(dataframe):
    try:
        print("\033[93m" + "Formatting the data..." + "\033[0m")
        # Remove the _id and user_id columns
        dataframe = dataframe.drop(columns=['_id', 'user_id'])

        label_encoder = LabelEncoder()

        # Encode the categorical features
        dataframe['breakfast'] = label_encoder.fit_transform(dataframe['breakfast'])
        dataframe['lunch'] = label_encoder.fit_transform(dataframe['lunch'])
        dataframe['dinner'] = label_encoder.fit_transform(dataframe['dinner'])

        # Convert date to day of the week
        dataframe['date'] = pd.to_datetime(dataframe['date']).dt.dayofweek

        print("\033[92m" + "Data successfully formatted!" + "\033[0m")
        return dataframe

    except Exception as e:
        print("\033[91m" + "An error occurred while formatting the data:", str(e) + "\033[0m")
        return None

# Split the data into training and evaluation sets
def get_training_data(dataframe, label_column, test_size=0.3, random_state=0):
    try:
        print("\033[93m" + "Splitting the data into training and evaluation sets..." + "\033[0m")
        train_dataframe, eval_dataframe, train_label, eval_label = train_test_split(
            dataframe.drop(label_column, axis=1),  
            dataframe[label_column],  
            test_size=test_size,
            random_state=random_state
        )
        print("\033[92m" + "Successfully split the data into training and evaluation sets!" + "\033[0m")
        return train_dataframe, eval_dataframe, train_label, eval_label

    except Exception as e:
        print("\033[91m" + "An error occurred while splitting the data into training and evaluation sets:", str(e) + "\033[0m")
        return None

# Get the feature columns I want to use for the model
def get_feature_columns(feature_names):
    try:
        print("\033[93m" + "Getting the feature columns..." + "\033[0m")
        feature_columns = []
        for feature_name in feature_names:
            feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))
        print("\033[92m" + "Successfully got the feature columns!" + "\033[0m")
        return feature_columns
    except Exception as e:
        print("\033[91m" + "An error occurred while getting the feature columns:", str(e) + "\033[0m")
        return None

# Convert to CSV file for testing
def convert_to_csv(df, filename):
    try:
        print("\033[93m" + "Converting the DataFrame to a CSV file..." + "\033[0m")
        df.to_csv(filename, index=False)
        print("\033[92m" + "Successfully converted the DataFrame to a CSV file!" + "\033[0m")
    except Exception as e:
        print("\033[91m" + "An error occurred while converting the DataFrame to a CSV file:", str(e) + "\033[0m")
        return None
