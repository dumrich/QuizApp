# Base Image
FROM python:3.8

#Environment Variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTRUNBYTECODE=1

# Set work dir
WORKDIR /code

#Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /code/
