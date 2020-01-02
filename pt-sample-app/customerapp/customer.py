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


def get_address(cust_id):
       
      params = (
         ('address', cust_id),
      )

      get_address = requests.get('http://service_addressapp:10013/address', params=params)
   
      return(get_address.content)



@app.route("/customer")
def get_customer():
   customerdetails = "Invalide customer..."
   customerID = request.args.get('customer')

   try:
      es = Elasticsearch(
            ['elasticsearch'],
            port=9200,
            verify_certs=False, timeout=60 
      )
   except Exception as esConnection:
      customerdetails = "ES Connection Error..."

   try:
      esresult = es.search(index="customer-*", 
            body={
                     "query": {
                        "match_phrase": {
                           "json.ID": customerID
                        }
                     }
                  }
            )
   except Exception as esQuery:
      customerdetails = "Error..."
      
  
   for customeris in esresult['hits']['hits']:
         customerdata = json.dumps(customeris['_source']['json']['Name'])
                  
         customeraddress = get_address(customerID)          
         customerdetails = customerdata + "," + str(customeraddress)

   return (customerdetails)


if __name__ == "__main__":
 app.run()
