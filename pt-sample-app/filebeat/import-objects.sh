#!bin/bash
sleep 5000
curl --silent -XPOST http://kibana:5601/api/saved_objects/_bulk_create -H 'Content-type:application/json' -H 'kbn-xsrf:true' -d@/etc/filebeat/pt-sampleapp-dashboards-12.json
curl --silent -XPOST http://kibana:5601/api/kibana/settings/defaultIndex -H "Content-Type: application/json" -H "kbn-xsrf: true" -d'{"value": "product-*"}'
