from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
import requests
import json
from config import key


k = 273.15

@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float
    
@dataclass(frozen=True)
class Weather:
    location: str
    temperature: float
    temperature_feelings: float
    temperature_max: float
    temperature_min: float
    description: str
    wind_speed: float
    wind_direction: str
    wind_gust: str
    sunrise: datetime
    sunset: datetime
    # icon: str
    
        
class WindDirection(IntEnum):
    North = 0
    NorthEast = 45
    East = 90
    SouthEast = 135
    South = 180
    SouthWest = 225
    West = 270
    NorthWest = 315

    
def get_ip_data():
    url = 'https://ipinfo.io/json/'
    data = requests.get(url)
    data = json.loads(data.text)
    return data

# def get_coordinates():
#     data = get_ip_data()
#     latitude = data['loc'].split(',')[0]
#     longitude = data['loc'].split(',')[1]
    
#     return Coordinates(latitude, longitude)

def get_weather(coordinates):
    data = get_weather_response(coordinates.latitude, coordinates.longitude)
    weather = parse_weather_response(data)
    return weather

def get_weather_response(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
    data = requests.get(url)
    data = json.loads(data.text)
    return data

def parse_weather_response(weather_response):
    data = weather_response
    return Weather(
        location=parse_location(data),
        temperature=parse_temperature(data),
        temperature_feelings=parse_temperature_feelings(data),
        temperature_max=parse_temperature_max(data),
        temperature_min=parse_temperature_min(data),
        description=parse_description(data),
        wind_speed=parse_wind_speed(data),
        wind_direction=parse_wind_direction(data),
        wind_gust=parse_wind_gust(data),
        sunrise=parse_suntime(data, 'sunrise'),
        sunset=parse_suntime(data, 'sunset'), 
        # icon=parse_icon(data)
    )

def parse_location(dict):
    return dict['name']

# def parse_icon(dict):
#     a = dict['weather'][0]['icon']
#     data = f'http://openweathermap.org/img/wn/{a}@2x.png'
#     # data = requests.get(url)
#     return data

def parse_temperature(dict):
    return round(float(dict['main']['temp']) - k, 1)

def parse_temperature_feelings(dict):
    return round(float(dict['main']['feels_like']) - k, 1)

def parse_temperature_max(dict):
    return round(float(dict['main']['temp_max']) - k, 1)

def parse_temperature_min(dict):
    return round(float(dict['main']['temp_min']) - k, 1)

def parse_description(dict):
    return dict['weather'][0]['description'].capitalize()


def parse_wind_speed(dict):
    return dict['wind']['speed']

def parse_wind_direction(dict):
    degrees = round(dict['wind']['deg'] / 45) * 45
    if degrees ==360: degrees = 0
    return WindDirection(degrees).name

def parse_wind_gust(dict):
    return dict['wind']['gust']

def parse_suntime(dict, time):
    return datetime.fromtimestamp(dict['sys'][time])