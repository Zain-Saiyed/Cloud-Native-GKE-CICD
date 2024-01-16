from flask import Flask,jsonify,request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
import os
import pandas as pd
from io import StringIO
import requests
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app and enable CORS
app=Flask(__name__)
CORS(app)

# Define the mount volume directory
file_path = "/gke_PV_dir/"

# Verify if a file exists
def verify_file_existence(filename):
    if not os.path.isfile(file_path+filename):
        return False
    return True

# Verify if a JSON key exists
def verify_json_key(key,tag):
    if key == tag:
        return True
    return False

# Read the content of an input file
def read_input_file(filename):
    file_content = StringIO(open(file_path+filename).read()) # https://www.w3schools.com/python/python_file_open.asp
    try:
        file_content = pd.read_csv(file_content)
    # Catch csv Parse error 
    except pd.errors.ParserError: # https://saturncloud.io/blog/what-is-parsererror-in-pythonpandas-and-how-to-fix-it/#:~:text=ParserError%20is%20an%20error%20that,a%20different%20number%20of%20fields.
        return [False,None]
    except:
        return [False,None]
    print("file content read success.")
    return [True,file_content]

# Get temperature data from file content
def get_temperature_data(name, file_content):
    # if name in file_content.columns:
    result_df = file_content[file_content["name"] == name]["temperature"].tail(1)
    if len(result_df) < 1:
         return [False,None]
    
    return [True, result_df]

# Route: Get temperature - to process JSON request and retrieve temperature data
@app.route('/get-temp',methods=['POST'])
def process_json_request():
    if request.method == 'POST':
        json_req = request.json
        
        logging.error("json_req : "+str(json_req))
        if  all(key not in json_req.keys() for key in ["file", "name", "key"]):
            return "error key not found"
        
        if json_req["file"] == None:
            return jsonify({"file":None,"error":"Invalid JSON input."})
        
        filename = request.json["file"]
        
        # if file not found return error message 
        if not verify_file_existence(filename):
            return jsonify({"file":filename,"error":"File not found."})
        
        name = request.json["name"]
        print("file ",filename)
        print("name ",name)
        
        
        status, file_content = read_input_file(filename)
        logging.error("status : "+str(status))
        logging.error("file_content : "+str(file_content))
        
        if not status:
            return jsonify({"file":filename,"error":"Input file not in CSV format."})
            
        print("file_content : \n",file_content)

        # Retrieve temperature data from file content
        status, temperature_data = get_temperature_data(name, file_content)
        logging.error("temperature_data : "+str(temperature_data))
        
        if not status:
            return jsonify({"file":filename,"error":"Data not found for 'name'='"+name+"'"}) # Input file not in CSV format
            
        print("temperature_data ",temperature_data)
        print("temperature -> ",temperature_data.values[0])
        # Return temperature data in JSON response
        return jsonify({"file":filename,"temperature":int(temperature_data.values[0])})
            
# Main entry point of the application
if __name__ == "__main__":
    # Run the Flask app using gevent WSGIServer
    http_server = WSGIServer(('', 6030), app)
    http_server.serve_forever()
    
# flask --app container2_app --debug run --host=0.0.0.0 --port=6030
# https://flask.palletsprojects.com/en/2.3.x/quickstart/
# https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/