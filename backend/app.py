from flask import Flask, request, jsonify

import backend.utils as utils 



app = Flask(__name__)
@app.route('/get_location_name')
def get_location_name():
    response = jsonify({
        "location_name": utils.get_location_name()
    })
    response.headers.add ('Access-control-allow-origin', '*')
    return response
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    pass

if __name__ == '__main__':
    print("Starting")
    app.run()