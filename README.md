# Code Challenge Template


## Project Setup
- Python Version: python>=3.9
- Create and activate a virtual environment - using Makefile or manual
  -  `make venv`
  or Manual
  - `python3 -m venv <env>`
  - `source <env>/bin/activate`
- Set Django settings
  - `export DJANGO_SETTINGS_MODULE="pipeline.settings"`
- Apply Database Migrations
  - `python3 manage.py migrate`

## Testcases
- Using Nosetests to run tests for the project:
  - `nosetests .`

## Data Ingestion
- Ingesting crop and weather data using following commands
  - `python3.9 manage.py import_weather_data`
  - `python3.9 manage.py import_crop_data`
  - please see the screenshot - Dataingestion for crop and weather data.png for reference in Answers folder

## Data Analysis
- Weather Stats are computed for pair of station_id and year possible using following command:
  - `python manage.py analyze_weather_data`
  - please see the screenshot - weather_analysis.png for reference in Answers folder

## REST APIs
- Django REST Framework was used to develop the following 3 REST API GET endpoints with default 
    pagination 50 records and filter arguments per assignment:
  - /api/weather 
  - /api/yield
  - /api/weather/stats

  Examples below and refer api postman screenshots in Answers folder for the following GET api responses:
  
  `http://localhost:8000/api/crop/?page=1`
  `http://localhost:8000/api/weather/?page=3`
  `http://localhost:8000/api/weather/stats?page=10`
  `http://localhost:8000/api/weather/stats?page=1&year=1986`
    
    
