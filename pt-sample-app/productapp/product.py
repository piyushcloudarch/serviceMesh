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
       
@app.route("/product")
def get_product():
   cust_product = "Invalide product..."
   productID = request.args.get('product')

   try:
      es = Elasticsearch(
            ['elasticsearch'],
            port=9200,
            verify_certs=False, timeout=60 
      )
   except Exception as esConnection:
      cust_product = "ES Connection Error..."
      
   try:
      esresult = es.search(index="product-*", 
            body={
                     "query": {
                        "match_phrase": {
                           "json.ID": productID
                        }
                     }
                  }
            )      
   except Exception as esQuery:
      cust_product = "Error..."   
      
  
   for productis in esresult['hits']['hits']:
         cust_product = json.dumps(productis['_source']['json']['Name'])
                  
   return (cust_product)


if __name__ == "__main__":
 app.run()
