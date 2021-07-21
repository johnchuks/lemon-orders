# Pull base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt
COPY ./requirements.txt  /requirements.txt

#Install dependencies
RUN pip install -r /requirements.txt

EXPOSE 6500

# Copy project
COPY . .

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 6500
