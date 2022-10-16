import requests
from bs4 import BeautifulSoup as b
  

url = "https://horo.mail.ru/prediction/sagittarius/today/"
def parse_horoscope_today(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope = soup.find_all('div', class_='article__text')
    horoscopes_today = [c.text for c in horoscope][0]
    return horoscopes_today

horoscopes_today = parse_horoscope_today(url)

url = "https://horo.mail.ru/prediction/sagittarius/tomorrow/"
def parse_horoscope_tomorrow(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope = soup.find_all('div', class_='article__text')
    horoscopes_tomorrow = [c.text for c in horoscope][0]
    return horoscopes_tomorrow

horoscopes_tomorrow = parse_horoscope_tomorrow(url)

url = "https://horo.mail.ru/prediction/sagittarius/week/"
def parse_horoscope_week(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope = soup.find_all('div', class_='article__text')
    horoscopes_week = [c.text for c in horoscope][0]
    return horoscopes_week

horoscopes_week = parse_horoscope_week(url)

url = "https://horo.mail.ru/prediction/sagittarius/month/"
def parse_horoscope_month(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    horoscope = soup.find_all('div', class_='article__text')
    horoscopes_month = [c.text for c in horoscope][0]
    return horoscopes_month

horoscopes_month = parse_horoscope_month(url)


