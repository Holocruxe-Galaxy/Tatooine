#%%
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from utils import data_utils

data = data_utils.get_dataframe()
predict = ['breakfast']
# drop 'dinner' and 'lunch' columns
data = data.drop(['dinner', 'lunch'], axis=1)
print(data.head())
# convert data to numpy array and drop the predict column
features = np.array(data.drop(predict, axis=1))
labels = np.array(data[predict])

features_train, features_evaluation, labels_train, labels_evaluation = train_test_split(features, labels, test_size=0.1)
model = linear_model.LinearRegression()
for i in range(10):
    model.fit(features_train, labels_train)
labels_prediction = model.predict(features_evaluation)
#print accuracy
accuracy = model.score(features_evaluation, labels_evaluation)
print(accuracy)
