import sys
from IPython.core.ultratb import ColorTB
sys.excepthook = ColorTB()

from utils import data_utils, model_utils
# get the data
dataframe = data_utils.get_dataframe()

# get training and evaluation data
train_dataframe, eval_dataframe, train_label, eval_label = data_utils.get_training_data(dataframe, 'breakfast')

print(train_dataframe.head())
print(eval_dataframe.head())
# generate the input functions
train_input = model_utils.generate_input(train_dataframe, train_label, num_epochs=10, shuffle=True)
eval_input = model_utils.generate_input(eval_dataframe, eval_label, num_epochs=1, shuffle=False)

# get the number of classes in breakfast column
n_classes = len(dataframe['breakfast'].unique())

# create the model
model = model_utils.create_linear_estimator(['date', 'lunch', 'dinner'], n_classes)

#save model
model.save('model.h5')

# train and evaluate the model
print(type(train_input))
print(type(eval_input))

result = model_utils.train(model, train_input, eval_input)

