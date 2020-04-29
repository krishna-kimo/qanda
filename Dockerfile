## Docker file for covid-QandA

## Basic Information
FROM python:3.6
LABEL maintainer="krishna@kimo.ai"
LABEL version="1.0"
LABEL description="The KIMO module for Covid QandA"

## Basic Setup
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


## Install required libraries/components
RUN pip install --no-cache -r requirements.txt

## Get the modified version of Ktrain and install
#RUN git clone https://github.com/krishna-kimo/ktrain.git ktrain
#WORKDIR /ktrain
#RUN python setup.py install

## Get the index from google bucket and untar it
#### The CURL command needs an output file name
#### Need to check if untaring is done properly or not
#WORKDIR /
RUN mkdir -p /tmp/index
RUN curl https://storage.googleapis.com/kqanda/index.tar.gz --output index.tar.gz
RUN tar -xzf index.tar.gz -C /tmp/index --strip-components 2

## Run the app
CMD exec gunicorn --bind :$PORT --workers 10 --threads 10 --timeout 0 app:app
