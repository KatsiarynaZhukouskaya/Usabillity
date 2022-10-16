from weatherData import get_weather
# from weatherData import get_coordinates
from horoscope import parse_horoscope_today, parse_horoscope_tomorrow, parse_horoscope_week, parse_horoscope_month
from horoscope import horoscopes_today, horoscopes_tomorrow, horoscopes_week, horoscopes_month
def weather(coordinates):
    data = get_weather(coordinates)
    return f'{data.location}\n\
{data.description}\n\
Температура воздуха 🌡 {data.temperature}°C\n\
По ощущениям: {data.temperature_feelings}°C\n\
Максимальная температура: {data.temperature_max}°C\n\
Минимальная температура: {data.temperature_min}°C'

def wind(coordinates):
    data = get_weather(coordinates)
    return f'Ветер {data.wind_direction}, скорость ветра {data.wind_speed} m/s🌬\n\
С порывами до 💨 {data.wind_gust} m/s'


def sun_time(coordinates):
    data = get_weather(coordinates)
    return f'Рассвет 🌝: {data.sunrise.strftime("%H:%M")}\n\
Закат 🌛: {data.sunset.strftime("%H:%M")}'


def start():
    return f"Привет, нажми кнопку ниже и выбери действие"

def start_weather():
    return f"Привет, для продолжения отправь свою геолокацию"


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

def zodiac():
    data = horoscopes_month
    return f'{data}'

   