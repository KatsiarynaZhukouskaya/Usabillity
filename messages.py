from weatherData import get_weather
# from weatherData import get_coordinates
from horoscope import parse_horoscope_today, parse_horoscope_tomorrow, parse_horoscope_week, parse_horoscope_month
from horoscope import horoscopes_today, horoscopes_tomorrow, horoscopes_week, horoscopes_month
def weather(coordinates):
    data = get_weather(coordinates)
    return f'{data.location}\n\
{data.description}\n\
Temperature is 🌡 {data.temperature}°C\n\
Feels like {data.temperature_feelings}°C\n\
Max temperature {data.temperature_max}°C\n\
Min temperature {data.temperature_min}°C'

def wind(coordinates):
    data = get_weather(coordinates)
    return f'{data.wind_direction} wind 🌬 {data.wind_speed} m/s\n\
Gust 💨 {data.wind_gust} m/s'


def sun_time(coordinates):
    data = get_weather(coordinates)
    return f'Sunrise 🌝: {data.sunrise.strftime("%H:%M")}\n\
Sunset 🌛: {data.sunset.strftime("%H:%M")}'


def start():
    return f"Hello, Send your GEO to continue"


def horoscope_today():
    data = horoscopes_today
    return f'{data}'

def horoscope_tomorrow():
    data = horoscopes_tomorrow
    return f'{data}'

def horoscope_week():
    data = horoscopes_week
    return f'{data}'

def horoscope_month():
    data = horoscopes_month
    return f'{data}'

   