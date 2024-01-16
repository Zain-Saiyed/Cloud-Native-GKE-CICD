FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN ls -lrt

RUN pip install -r requirements.txt

EXPOSE 6030

cmd ["flask","--app","container2_app","run","--host=0.0.0.0","--port=6030"]