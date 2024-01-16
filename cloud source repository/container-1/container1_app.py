from flask import Flask, jsonify, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
import os
import pandas as pd
from io import StringIO
import requests

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Define the mount volume directory
file_path = "/gke_PV_dir/"

# Check if a file exists
def verify_file_existence(filename):
    if not os.path.isfile(file_path + filename):
        return False
    return True

# Verify if a JSON key exists
def verify_json_key(key, tag):
    if key == tag:
        return True
    return False

# Read the content of an input file
def read_input_file(filename):
    print("Entered read_input_file  ")
    file_content = StringIO(open(file_path + filename).read())
    try:
        file_content = pd.read_csv(file_content)
        # Minimum 4 columns should be present
        print("columns : ", len(file_content.columns.values))
        if len(file_content.columns.values) != 4:
            return [False, None]
    except pd.errors.ParserError:
        print("Exception occurred read_input_file")
        return [False, None]
    except:
        return [False, None]
    # If content is empty then False
    if file_content.empty:
        return [False, None]
    print("file content read success.")
    return [True, file_content]

# Get location data from the file content
def get_location_data(name, file_content):
    result_df = file_content[file_content["name"] == name][["latitude", "longitude"]].tail(1)
    if len(result_df) < 1:
        return [False, None]
    return [True, result_df]

# Check if keys are present in the JSON request
def check_if_keys_present(key_name, json_req):
    print(f"{key_name} not in {json_req.keys()} : ", key_name not in json_req.keys())
    if key_name not in json_req.keys():
        return False
    elif json_req[key_name] == None:
        return False
    else:
        return True

# Route: Store file- to handle storing a file
@app.route('/store-file', methods=['POST'])
def store_file_request():
    if request.method == 'POST':
        json_req = request.json
        print("json_req : ", json_req)
        print("json_req.keys() : ", json_req.keys())

        # Check if "file" key is present in JSON request
        if check_if_keys_present("file", json_req):
            filename = request.json["file"]
        else:
            return jsonify({"file": None, "error": "Invalid JSON input."})

        try:
            # Write data to the specified file
            with open(file_path + filename, 'w') as f:
                f.write(request.json["data"])
            return jsonify({"file": filename, "message": "Success."})

        except:
            return jsonify({"file": filename, "error": "Error while storing the file to the storage."})

# Route: Get temperature- to get temperature information
@app.route('/get-temperature', methods=['POST'])
def get_temperature_request():
    if request.method == 'POST':
        json_req = request.json
        print("json_req : ", json_req)
        print("json_req.keys() : ", json_req.keys())

        # Check if necessary keys are present in JSON request
        if all(key not in json_req.keys() for key in ["file", "name", "key"]):
            return "error key not found"

        # Check if "file" key is present in JSON request
        if check_if_keys_present("file", json_req):
            filename = request.json["file"]
        else:
            return jsonify({"file": None, "error": "Invalid JSON input."})

        # Check if file exists
        if not verify_file_existence(filename):
            return jsonify({"file": filename, "error": "File not found."})

        status, file_content = read_input_file(filename)
        print("file_content: ", file_content)
        print("status :", status)

        # Check if input file is in CSV format
        if not status:
            return jsonify({"file": filename, "error": "Input file not in CSV format."})

        print("file_content : \n", file_content)

        print("sending request to the second API")
        # Send request to the second API
        response = requests.post('http://container-2-service:6030/get-temp', json=json_req)
        if response.status_code == 200:
            return response.json()

# Main entry point of the application
if __name__ == "__main__":
    # Run the Flask app using gevent WSGIServer
    http_server = WSGIServer(('', 6000), app)
    http_server.serve_forever()

# flask --app container1_app run --host=0.0.0.0 --port=6000
# https://flask.palletsprojects.com/en/2.3.x/quickstart/
