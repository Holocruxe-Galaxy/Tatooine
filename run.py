from utils import debug_utils
from utils.data_utils import Data
from utils.model_utils import Model

logger = debug_utils.logger

# Create the Data instance with the OneHotEncoder encoding type
data = Data(encoder="label_encoder")
model = Model(data.dataframe, 'food')
model.evaluate_model(model.features_evaluation, model.labels_evaluation)
