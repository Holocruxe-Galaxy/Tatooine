import sys
from utils import data as data_utils, model as model_utils, debug as debug_utils
logger = debug_utils.logger


# Get the data
data = data_utils.get_data()
print(data)