FROM python:3.8.1-buster

LABEL Nemira Fedor

RUN pip3 install uwsgi

COPY . /project

WORKDIR /project

RUN pip3 install -r ./requirements.txt

CMD uwsgi --http 0.0.0.0:8888 --master --module project.wsgi --processes 8 --http-timeout 700

 
