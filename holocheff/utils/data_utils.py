

import pandas as pd
import tensorflow as tf
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def test():
    print("data_utils is working.")

# Import the data from MongoDB and convert it to a pandas DataFrame
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

        # Format the data
        dataframe = format_data(dataframe)
        
        return dataframe
    except Exception as e:
        print("An error occurred while retrieving the data:", str(e))

# Format the data
def format_data(dataframe):
    try:
        # Remove the _id and user_id columns
        dataframe = dataframe.drop(columns=['_id', 'user_id'])

        label_encoder = LabelEncoder()

        # Encode the categorical features
        dataframe['breakfast'] = label_encoder.fit_transform(dataframe['breakfast'])
        dataframe['lunch'] = label_encoder.fit_transform(dataframe['lunch'])
        dataframe['dinner'] = label_encoder.fit_transform(dataframe['dinner'])

        # Convert date to day of the week
        dataframe['date'] = pd.to_datetime(dataframe['date']).dt.dayofweek

        return dataframe

    except Exception as e:
        print("An error occurred during data formatting:", str(e))
        return None

# Split the data into training and evaluation sets
def get_training_data(df, label_column, test_size=0.3, random_state=0):
    try:
        train_df, eval_df, train_label, eval_label = train_test_split(
            df.drop(label_column, axis=1), df[label_column], test_size=test_size, random_state=random_state
        )
        return train_df, eval_df, train_label, eval_label

    except Exception as e:
        print("An error occurred while getting training data:", str(e))
        return None

# Get the labels I want to predict from the DataFrame
def get_labels(df, label_column):
    return df[label_column]

# Get the feature columns I want to use for the model
def get_feature_columns(feature_names):
    feature_columns = []
    for feature_name in feature_names:
        feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))
    return feature_columns

# Convert to csv file for testing
def convert_to_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print("An error occurred while converting the DataFrame to a CSV file:", str(e))