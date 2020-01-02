FROM envoyproxy/envoy-alpine:latest
MAINTAINER PT "TekP@gmail.com"

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN apk add --no-cache curl

COPY envoy-customer.yaml /etc/envoy/envoy.yaml
ENTRYPOINT ["/bin/sh", "-c", "python customer.py & /usr/local/bin/envoy -c /etc/envoy/envoy.yaml"]

EXPOSE 10012