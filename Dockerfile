# pull official base image
FROM python:3.9-slim-buster as base@sha256:d8e4e87bb3c774fefc697c0d8b25faa7aaa775e5537a194f37d2d767049b631f

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install app dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

########
# Test #
########
FROM base
RUN pytest --cov=project tests/

###############
# Development #
###############
FROM base