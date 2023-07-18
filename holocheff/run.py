import pandas as pd
import numpy as np
import pickle

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
from utils import data_utils
import datetime

# Get the data
data = data_utils.get_dataframe()
# Format the data
data = data_utils.format_data(data)

# Get the predict columns
predict = ['breakfast', 'lunch', 'dinner']

# Convert data to numpy array and drop the predict columns
features = np.array(data.drop(predict, axis=1))
labels = np.array(data[predict])

# Split the data into training and testing sets
features_train, features_evaluation, labels_train, labels_evaluation = train_test_split(features, labels, test_size=0.3)

# Create the model
model = LinearRegression()

# Train the model
model.fit(features_train, labels_train)

# Predict the next meal
labels_prediction = model.predict(features_evaluation)

# Save the model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

# # Load the model
# model = pickle.load(open('model.pkl', 'rb'))

# Print accuracy in percentage
print(model.score(features_evaluation, labels_evaluation) * 100)

# Print the next meal
print(labels_prediction[-1][0])
