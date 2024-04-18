from flask import Flask, request, jsonify

import backend.utils as utils


app = Flask(__name__)
@app.route('/get_location_name')
def get_location_name():
    response = jsonify({
        "locations": utils.get_location_name()
    })
    response.headers.add ('Access-control-allow-origin', '*')
    return response
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])

    response = jsonify({
        'estimated_price' : utils.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add ('Access-control-allow-origin', '*')
    return response

if __name__ == '__main__':
    print("Starting")
    app.run()