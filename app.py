from flask import Flask, request, jsonify

import utis 



app = Flask(__name__)
@app.route('/get_location_name')
def get_location_name():
    response = jsonify({
        "location_name": utis.get_location_name()
    })
    response.headers.add ('Access-control-allow-origin', '*')
    return response

if __name__ == '__main__':
    print("Starting")
    app.run()