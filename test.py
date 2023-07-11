#%%
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from pymongo import MongoClient

# ----------1. get_dataframe----------#
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['holocheff_db_test']
collection = database['meals']

# Query the data from MongoDB
data = collection.find({})

# Convert MongoDB data to pandas DataFrame
dataframe = pd.DataFrame(list(data))

# ----------2. format_data----------#
label_encoder = LabelEncoder()

# Encode the categorical features
dataframe['breakfast'] = label_encoder.fit_transform(dataframe['breakfast'])
dataframe['lunch'] = label_encoder.fit_transform(dataframe['lunch'])
dataframe['dinner'] = label_encoder.fit_transform(dataframe['dinner'])

# Convert date to day of the week
dataframe['date'] = pd.to_datetime(dataframe['date']).dt.dayofweek

# Split the data into training and evaluation sets
train_dataframe, eval_dataframe, train_label, eval_label = train_test_split(
    dataframe.drop('breakfast', axis=1), dataframe['breakfast'], test_size=0.3, random_state=0)

# ----------3. CREATE THE INPUT FUNCTION----------#
# Create input functions for training and evaluation
train_input_fn = tf.compat.v1.estimator.inputs.pandas_input_fn(
    x=train_dataframe,
    y=train_label,
    num_epochs=10,
    shuffle=True,
    batch_size=32
)

eval_input_fn = tf.compat.v1.estimator.inputs.pandas_input_fn(
    x=eval_dataframe,
    y=eval_label,
    num_epochs=1,
    shuffle=False
)

# ----------4. CREATE THE MODEL----------#
# Create a list of feature columns for the model
feature_columns = []
for feature_name in ['date', 'lunch', 'dinner']:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

# Create a linear estimator
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns, n_classes=10)  # Update n_classes with the correct number of classes

# Train the model
linear_est.train(train_input_fn)

# Evaluate the model
result = linear_est.evaluate(eval_input_fn)
# print(result['accuracy'])

# ----------5. PREDICT----------#
# Get predictions from the model
predictions = list(linear_est.predict(eval_input_fn))

# clear the notebook
from IPython.display import clear_output
clear_output(wait=True)
# print the next breakfast as a string
print("The next breakfast is: ", label_encoder.inverse_transform([predictions[0]['class_ids'][0]]))

# %%
