# rakt

# Food Truck Finder Project

## Overview
The Food Truck Finder is a Django application that allows users to find the nearest food trucks based on their current latitude and longitude.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.10+
- Pip (Python package manager)
- Virtual environment (optional)
- Docker (recommended)

## Setup with Docker

1. **Build and run the Docker Image**
   ```bash
   docker-compose up --build
 - Unit tests will automatically run

2. **Access the Application**
   - The application will be available at http://0.0.0.0:8000/food_truck/food_trucks/
   - You can also use restful api at http://0.0.0.0:8000/food_truck/find_nearby/

## Manual setup

1. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   
  ### Activate the virtual environment:
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
        
   - On Windows:
     ```bash
     source venv/bin/activate

2. **Install Requirements**
   - Install the required packages using pip:
    ```bash
    cd foodfinder/
    pip install -r requirements.txt

3. **Create and Apply Migrations**
   - Create the migrations for your database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

  ### Testing
- For automated tests, run:
   ```bash
   python manage.py test

4. **Access the Application**
   - The application will be available at http://127.0.0.1:8000/food_truck/food_trucks/
   - You can also use restful api at http://127.0.0.1:8000/food_truck/find_nearby/
