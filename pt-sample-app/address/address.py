from flask import Flask, jsonify, request
import requests
import json
from flask_cors import CORS
from elasticsearch import Elasticsearch

app = Flask(__name__)
CORS(app)

@app.route("/health")
def get_health():
       return ("True")
       
@app.route("/address")
def get_address():
   cust_address = "Invalide Address..."
   addressID = request.args.get('address')

   try:
      es = Elasticsearch(
            ['elasticsearch'],
            port=9200,
            verify_certs=False, timeout=60 
      )
   except Exception as esConnection:
      cust_address = "ES Connection Error..."

   try:
      esresult = es.search(index="address-*", 
            body={
                     "query": {
                        "match_phrase": {
                           "json.CustID": addressID
                        }
                     }
                  }
            )
   except Exception as esQuery:
      cust_address = "Error..."
      
  
   for addressis in esresult['hits']['hits']:
         cust_address = json.dumps(addressis['_source']['json']['Address'])
                  
   return (cust_address)


if __name__ == "__main__":
 app.run()
