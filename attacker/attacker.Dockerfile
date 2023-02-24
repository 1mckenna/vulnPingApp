# Dockerfile
FROM alpine:latest
WORKDIR /tmp
RUN apk update && apk add nmap-ncat bash
CMD ["tail", "-f","/dev/null"]
