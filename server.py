from flask import Flask, request, render_template, jsonify
import json
import numpy as np
import pickle

app = Flask(__name__)

# Load data during startup
with open("data/columns.json", 'r') as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]

with open("data/bhpp.pickle", 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def estimate_price():
    data = request.form
    location = data['location']
    print("1st print",location)
    sqft = float(data['sqft'])
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    # Check if location exists in the location_data dictionary
    if location not in locations:
        print("2nd one",location)
        print("locations",locations)
        return jsonify({'error': 'Invalid location'}), 400

    loc_index = locations.index(location)

    input_features = np.zeros(len(data_columns))
    input_features[0] = sqft
    input_features[1] = bath
    input_features[2] = bhk
    if loc_index >= 0:
        input_features[loc_index + 3] = 1

    predicted_price = round(model.predict([input_features])[0], 2)
    print("Estimated price", predicted_price)
    # Pass the estimated price directly to the template
    return render_template('index.html', locations=locations, predicted_price=predicted_price)

if __name__ == '__main__':
    print("Starting")
    app.run()
