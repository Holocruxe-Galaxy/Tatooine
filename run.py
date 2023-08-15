
from utils.data_utils import Data
from utils.model_utils import Model
from flask import Flask, request, jsonify
app = Flask(__name__)


# Create the Data instance with the OneHotEncoder encoding type
def Main():
    data = Data('user0').get_meals()
    model = Model(data)
    model_output = model.output()
    input_hook()
    return model_output

@app.route('/input', methods=['POST'])
def input_hook():
    # Parse the input data from the request
    input_data = request.json
    print(input_data)
    # TODO: Process the input data    
    return 'Input received'

@app.route('/output', methods=['GET'])
def output_hook():
    # Call the Main function to get the model output
    model_output = Main()
    # TODO: Process the model output
    return jsonify(model_output)
if __name__ == "__main__":
    app.run()
