FROM python:3.9.1
ADD . /trocadilhosbot
WORKDIR /trocadilhosbot
RUN pip install -r requirements.txt

EXPOSE 5000