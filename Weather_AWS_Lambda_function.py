import json
import pandas as pd
import requests
import sqlalchemy
from keys import weather_key as wkey
from keys import gans_aws_key as awskey

def get_weather_forecast(cities_df, wkey):
    # Initialize an empty dictionary to store weather forecast data
    weather_forecast = {
        'city_id': [],
        'time': [],
        'current_temp': [],
        'forecast_temp': [],
        'feels_like': [],
        'humidity_level': []
    }
    
    # Iterate over each city in the cities DataFrame
    for i, row in cities_df.iterrows():
        city_id = row['city_id']
        city_name = row['city_name']

        # Form the URL for fetching weather data
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={wkey}&units=metric"

        # Make the API request
        response = requests.get(url)
        
        # Print response status for debugging purposes
        print(f"Response status code for city {city_name}: {response.status_code}")

        # If the response status is not 200 (OK), print an error and continue to the next city
        if response.status_code != 200:
            print(f"Error fetching data for city {city_name}. Status code: {response.status_code}")
            continue 

        # Parse the JSON response
        weather_forecast_json = response.json()
        
        # Extract relevant information from the response and append to the weather_forecast dictionary
        for time in weather_forecast_json['list']:  
            weather_forecast['city_id'].append(city_id)
            weather_forecast['time'].append(time['dt_txt'])
            weather_forecast['current_temp'].append(time['main']['temp'])
            weather_forecast['forecast_temp'].append(time['weather'][0]['main'])
            weather_forecast['feels_like'].append(time['main']['feels_like'])
            weather_forecast['humidity_level'].append(time['main']['humidity'])

    # Convert the weather_forecast dictionary to a pandas DataFrame and return
    weather_forecast_df = pd.DataFrame(weather_forecast)
    return weather_forecast_df

def valid_city_id(city_id, con):
    # Check if the given city_id exists in the cities table in the database
    query = "SELECT 1 FROM cities WHERE city_id = %s"
    result = pd.read_sql(query, con=con, params=(city_id,))
    return not result.empty

def lambda_handler(event, context):
    # Database connection details
    host = 'wbs-gans-jh-project.cye0p6hkvuel.us-east-1.rds.amazonaws.com'
    schema = 'gans_aws_JH'
    user = 'admin'
    password = awskey
    port = 3306
    con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'
    
    # Fetch city data from the database
    cities_df = pd.read_sql('cities',con=con)

    # Fetch weather forecast data for the cities
    weather_forecast_df = get_weather_forecast(cities_df, wkey)

    # Filter out rows with invalid city_ids
    weather_forecast_df = weather_forecast_df[weather_forecast_df['city_id'].apply(valid_city_id, con=con)]
    
    # Define the data types for the columns in the weather table
    data_types = {
        'city_id': sqlalchemy.types.Integer,
        'time': sqlalchemy.types.DateTime,
        'current_temp': sqlalchemy.types.Float,
        'forecast_temp': sqlalchemy.types.VARCHAR(40),
        'feels_like': sqlalchemy.types.Float,
        'humidity_level': sqlalchemy.types.Integer
    }

    # Insert the weather forecast data into the weather table in the database
    weather_forecast_df.to_sql('weather', con=con, dtype=data_types, if_exists='append', index=False)
    print(f'The weather table has been updated with {weather_forecast_df.shape[0]} records.')
    
    # Return a success status
    return {
        'statusCode': 200
    }
