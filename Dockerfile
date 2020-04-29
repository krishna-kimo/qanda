## Docker file for covid-QandA

## Basic Information
FROM python:3.6
LABEL maintainer="krishna@kimo.ai"
LABEL version="1.0"
LABEL description="The KIMO module for Covid QandA"

## Install required libraries/components
RUN apt-get install curl
RUN pip install "tensorflow==2.1.0"
RUN pip install torch torchvision

## Get the modified version of Ktrain and install
RUN git clone https://github.com/krishna-kimo/ktrain.git ktrain
WORKDIR /ktrain
RUN python setup.py install

## Get the index from google bucket and untar it
#### The CURL command needs an output file name
#### Need to check if untaring is done properly or not
WORKDIR /
RUN mkdir -p /tmp/index
RUN curl https://storage.googleapis.com/kqanda/index.tar.gz --output index.tar.gz
RUN tar -xzf index.tar.gz /tmp/index --strip-components 1

## Run Flask app



