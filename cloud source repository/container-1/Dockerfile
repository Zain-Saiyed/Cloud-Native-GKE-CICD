FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN ls -lrt

RUN pip install -r requirements.txt

EXPOSE 6000

CMD ["flask", "--app", "container1_app:app", "run", "--host=0.0.0.0", "--port=6000"]
