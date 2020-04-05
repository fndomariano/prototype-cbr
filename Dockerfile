FROM python:3.8.0-alpine

RUN apk update && \    
	apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# copy project
COPY . /app/