import requests
import time

##############set default index
time.sleep(10)


headers = {
    'Content-Type': 'application/json',
    'kbn-xsrf': 'true',
}

data = {'value': 'product-*'}

response = requests.post('http://kibana:5601/api/kibana/settings/defaultIndex', headers=headers, data=data)

print("default index set...")


##################upload objects
time.sleep(60)

headers = {
    'Content-type': 'application/json',
    'kbn-xsrf': 'true',
}

data = open('pt-sampleapp-dashboards-12.json')
response = requests.post('http://kibana:5601/api/saved_objects/_bulk_create', headers=headers, data=data)

print("object uploaded...")
