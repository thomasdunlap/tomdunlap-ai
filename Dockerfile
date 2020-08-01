from ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y build-essential python3 python3-pip

COPY . /webapp
WORKDIR /webapp

RUN pip3 install -r requirements.txt

EXPOSE 8001

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
