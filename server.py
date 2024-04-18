from flask import Flask, request, jsonify, render_template
import json
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

global __location
global __model
global __data_column

__data_column = None
__location = {}

# Load model and location data during startup
with open("data/columns.json", 'r') as f:
    __data_column = json.load(f)['data_columns']
    __location = {location.lower(): index for index, location in enumerate(__data_column[3:])}

with open("data/banglore_9.pickle", 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def estimate_price():
    data = request.form
    location = data['location']
    print('Location: ',location)
    sqft = float(data['sqft'])
    print('Sqft: ',sqft)
    bhk = int(data['bhk'])
    print('BHK: ',bhk)
    bath = int(data['bath'])
    print('Bath: ',bath)

    # Check if location exists in the location_data dictionary
    if location.lower() not in __location:
        return jsonify({'error': 'Invalid location'}), 400

    loc_index = __location[location.lower()]

    input_features = np.zeros(len(__data_column))
    input_features[0] = sqft
    input_features[1] = bath
    input_features[2] = bhk
    if loc_index >= 0:
        input_features[loc_index + 3] = 1

    estimated_price = round(model.predict([input_features])[0], 2)
    print("Estimated price", estimated_price)
    # Pass the estimated price directly to the template
    return render_template('predict.html', estimated_price=estimated_price)

if __name__ == '__main__':
    print("Starting")
    app.run()
