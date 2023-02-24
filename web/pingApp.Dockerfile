# Dockerfile
FROM python:3.12.0a5-alpine3.17
WORKDIR /srv
RUN apk update && apk add nmap-ncat bash
RUN pip install --upgrade pip
RUN pip install flask
ADD  templates/ /srv/templates/
COPY ping.py /srv
ENV FLASK_APP=ping
CMD ["python","ping.py"]
