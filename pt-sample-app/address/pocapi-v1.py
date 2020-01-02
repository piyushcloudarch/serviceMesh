from flask import Flask, jsonify, request
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/health")
def get_health():
       return ("True")
 
@app.route("/version")
def get_version():
       return ("version:v1")

if __name__ == "__main__":
 app.run()
