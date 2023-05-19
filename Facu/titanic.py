# %%

from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np  # multidimensional calculus library
import matplotlib.pyplot as plt  # plotting library
# from six.moves import urllib
# import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf


# El objetivo es predecir si un pasajero sobrevivirá o no al Titanic

# Load dataset.
dftrain = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/train.csv')  # training data
dfeval = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/eval.csv')  # testing data

# saca la columna survived del dataset y la guarda en y_train
y_train = dftrain.pop('survived')
# saca la columna survived del dataset y la guarda en y_eval
y_eval = dfeval.pop('survived')

# print(dftrain.head())  # muestra las 5 primeras filas del dataset
print(dftrain.describe())  # muestra estadísticas del dataset
# print(dftrain.shape) # muestra la cantidad de filas y columnas del dataset

dftrain.age.hist(bins=20)  # muestra un histograma de la columna age

# %%
