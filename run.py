from utils import debug_utils as debug_utils
from utils import data_utils as data_utils
import model

logger = debug_utils.logger


# Get the data
data = data_utils.get_data()

# Format the data
data = data_utils.format_data_OneHotEncoder(data)


model = model.ModelUtils(data, 'food')


