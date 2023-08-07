from utils import debug_utils
from utils.data_utils import Data
from utils.model_utils import Model

logger = debug_utils.logger

# Create the Data instance with the OneHotEncoder encoding type
def Main():
    data = Data('user0').get_meals()
    model = Model(data)
    model.output()

if __name__ == "__main__":
    Main()
