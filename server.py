from flask import Flask, request, jsonify, render_template
import json
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load model and location data during startup
with open("data/column.json", 'r') as f:
    location_data = json.load(f)

with open("data/bhpp.pickle", 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def estimate_price():
    data = request.get_json()
    location = data['location']
    sqft = data['sqft']
    bhk = data['bhk']
    bath = data['bath']

    try:
        loc_index = location_data.index(location.lower())
    except ValueError:
        return jsonify({'error': 'Invalid location'}), 400

    input_features = np.zeros(len(location_data))
    input_features[0] = sqft
    input_features[1] = bath
    input_features[2] = bhk
    if loc_index >= 0:
        input_features[loc_index] = 1

    estimated_price = round(model.predict([input_features])[0], 2)

    # Pass the estimated price directly to the template
    return render_template('predict.html', estimated_price=estimated_price)

if __name__ == '__main__':
    print("Starting")
    app.run()
