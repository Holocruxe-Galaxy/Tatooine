import pandas as pd
import numpy as np
import pickle

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
from utils import data_utils
import datetime

data = data_utils.get_dataframe()
data = data_utils.format_data(data)

# Determine the current time
current_time = datetime.datetime.now().time()
predict = ['breakfast', 'lunch', 'dinner']


# Convert data to numpy array and drop the predict column
features = np.array(data.drop(predict, axis=1))
labels = np.array(data[predict])

features_train, features_evaluation, labels_train, labels_evaluation = train_test_split(features, labels, test_size=0.3)

model = LinearRegression()

model.fit(features_train, labels_train)

labels_prediction = model.predict(features_evaluation)

with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

model = pickle.load(open('model.pkl', 'rb'))
# Print accuracy in percentage
print(model.score(features_evaluation, labels_evaluation) * 100)

# Print the next meal
print(labels_prediction[-1][0])
