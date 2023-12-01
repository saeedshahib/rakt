# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Install dependencies
# Copy the requirements.txt file into the container at /app
COPY foodfinder/requirements.txt /app/requirements.txt
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
# This assumes your manage.py is in the same directory as your Dockerfile
COPY . /app/
