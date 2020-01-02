FROM envoyproxy/envoy-alpine:latest
MAINTAINER PT "TekP@gmail.com"

RUN apk add --no-cache curl

COPY envoy-frontproxy.yaml /etc/envoy/envoy.yaml
ENTRYPOINT ["/bin/sh", "-c", "/usr/local/bin/envoy -c /etc/envoy/envoy.yaml"]

EXPOSE 10000