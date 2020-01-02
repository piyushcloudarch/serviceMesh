FROM docker.elastic.co/beats/filebeat:6.5.4

COPY --chown=filebeat:filebeat product.data /etc/filebeat/product.data
COPY --chown=filebeat:filebeat customer.data /etc/filebeat/customer.data
COPY --chown=filebeat:filebeat address.data /etc/filebeat/address.data

COPY --chown=filebeat:filebeat filebeat.yml /etc/filebeat/filebeat.yml

ENTRYPOINT ["/bin/bash", "-c", "/usr/share/filebeat/filebeat -c /etc/filebeat/filebeat.yml"]
