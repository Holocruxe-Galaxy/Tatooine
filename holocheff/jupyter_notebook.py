
#%%
from utils import data_utils, model_utils
# get the data
dataframe = data_utils.get_dataframe()
# generate the input functions
train_input = model_utils.generate_input(dataframe, data_utils.get_labels(dataframe, 'breakfast'))
eval_input = model_utils.generate_input(dataframe, data_utils.get_labels(dataframe, 'breakfast'), num_epochs=1, shuffle=False)
# get the number of classes in breakfast column
n_classes = len(dataframe['breakfast'].unique())
# create the model
model = model_utils.create_linear_estimator(['date', 'lunch', 'dinner'], n_classes)
# train and evaluate the model
result = model_utils.train(model, train_input, eval_input)
# print the result
print(result)





# %%
