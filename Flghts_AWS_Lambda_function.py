import json
import pandas as pd
import requests
import sqlalchemy
from keys import flights_key as fkey
from keys import gans_aws_key as awskey
from datetime import datetime, timedelta
from pytz import timezone



# Define the time intervals for fetching flight details
times = [["00:00", "11:59"], ["12:00", "23:59"]]


def get_city_id_mapping(con):
    cities_df = pd.read_sql('SELECT city_id, city_name FROM cities', con=con)
    return cities_df.set_index('city_name')['city_id'].to_dict()


# Function to fetch flight details for a given ICAO
def fetch_flights(icao, time_range):
    
    # API call settings
    headers = {
        "X-RapidAPI-Key": fkey,
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
    }
    
    querystring = {
        "withLeg": True,
        "direction": "Arrival",
        "withCancelled": False,
        "withCodeshared": False,
        "withCargo": False,
        "withPrivate": True,
        "withLocation": False
    }
    
    
    
    # Calculate tomorrow's date
    today = datetime.now().astimezone(timezone('Europe/Paris')).date()
    tomorrow = today + timedelta(days=1)
    
    url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{icao}/{tomorrow}T{time_range[0]}/{tomorrow}T{time_range[1]}"
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for ICAO: {icao} at time range: {time_range}. Error: {e}")
        return None


# Function to extract flight details from API response and populate into a DataFrame

def extract_flight_data(flights, icao, flights_df, city_id_mapping):
    for flight in flights.get('arrivals', []):
        flights_df['icao_id'].append(icao)
        
        # Getting the terminal info
        flights_df['arrival_terminal'].append(flight['arrival'].get('terminal'))
        
        # Getting the scheduled and revised arrival time
        scheduled_time = flight['arrival']['scheduledTime'].get('local', None)
        revised_time = flight['arrival'].get('revisedTime', {}).get('local', scheduled_time)
        flights_df['arrival_local_time'].append(revised_time)
        
        # Extracting the city name and corresponding city_id
        arrival_city = flight['departure']['airport'].get('name', None)
        city_id = city_id_mapping.get(arrival_city, None)
        flights_df['arrival_from_where'].append(arrival_city)
        flights_df['city_id'].append(city_id)
        
        # Extracting other details
        flights_df["flight_number"].append(flight.get("number", None))
        flights_df["flight_status"].append(flight.get("status", None))
        
        aircraft_model = flight.get('aircraft', {}).get('model', None)
        flights_df["airplane_model"].append(aircraft_model)
        
        flights_df["airline_name"].append(flight['airline'].get("name", None))
        
        depart_icao = flight['departure']['airport'].get('icao', None)
        flights_df["depart_icao"].append(depart_icao)


# Main Lambda function handler
def lambda_handler(event, context):
  
    # Database connection details
    host = 'wbs-gans-jh-project.cye0p6hkvuel.us-east-1.rds.amazonaws.com'
    schema = 'gans_aws_JH'
    user = 'admin'
    password = awskey
    port = 3306
    con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'
    
    # Fetch the city ID mapping
    city_id_mapping = get_city_id_mapping(con)

    # Initialize the flights dataframe
    flights_df = {
        'icao_id': [],
        'arrival_terminal': [],
        'arrival_local_time': [],
        'arrival_from_where': [],
        'flight_number': [],
        'flight_status': [],
        'airplane_model': [],
        'airline_name': [],
        'depart_icao': [],
        'city_id': []
    }

    airport_list_df = pd.read_sql('SELECT icao_id FROM airports', con=con)

    for icao in airport_list_df["icao_id"]:
        for time_range in times:
            flights = fetch_flights(icao, time_range)
            if flights:
                extract_flight_data(flights, icao, flights_df, city_id_mapping)

    # Convert the dictionary to a DataFrame
    flights_df = pd.DataFrame(flights_df)
    
    data_types = {
    'icao_id': sqlalchemy.types.String(length=50),
    'arrival_terminal': sqlalchemy.types.Integer,
    'arrival_local_time': sqlalchemy.types.DateTime,
    'arrival_from_where': sqlalchemy.types.String(length=50),
    'flight_number': sqlalchemy.types.String(length=50),
    'flight_status': sqlalchemy.types.String(length=50),
    'airplane_model': sqlalchemy.types.String(length=50),
    'airline_name': sqlalchemy.types.String(length=50),
    'depart_icao': sqlalchemy.types.String(length=50),
    'city_id': sqlalchemy.types.Integer,
    }

    # Ensure to establish the database connection within a context to auto close it after usage
    with sqlalchemy.create_engine(con).connect() as con:
        try:
            flights_df.to_sql('flights', con=con, if_exists='append', index=False, dtype=data_types)
            print(f'The flights table has been updated with {flights_df.shape[0]} records.')
        except Exception as e:
        
            print(f"Database insertion error: {e}")

    # Return a success status
    return {
        'statusCode': 200
    }