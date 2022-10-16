from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from models import January, February, March, April, May, June, July, August, September, October, November, December


BTN_START_WEATHER = KeyboardButton('Отправить мою локацию🗺',
                           request_location=True,
                           resize_keyboard=True,
                           one_time_keyboard=True)
BTN_WEATHER = InlineKeyboardButton('🌦Погода❄️', callback_data='weather')
BTN_WIND = InlineKeyboardButton('💨Ветер💨', callback_data='wind')
BTN_SUN_TIME = InlineKeyboardButton('Рассвет☀️ и закат🌙', callback_data='sun_time')
BTN_HOROSCOPE = InlineKeyboardButton("Выберите гороскоп")
BTN_HOROSCOPE_TODAY = InlineKeyboardButton('Гороскоп на сегодня:', callback_data='horoscope_today')
BTN_HOROSCOPE_TOMORROW = InlineKeyboardButton('Гороскоп на завтра:', callback_data='horoscope_tomorrow')
BTN_HOROSCOPE_WEEK = InlineKeyboardButton('Гороскоп на неделю:', callback_data='horoscope_week')
BTN_HOROSCOPE_MONTH = InlineKeyboardButton('Гороскоп на месяц:', callback_data='horoscope_month')

# keyboard_horoscope = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)

BTN_HOROSCOPE_ARIES = InlineKeyboardButton('♈ Овен ♈', callback_data='zodiac')
BTN_HOROSCOPE_TAURUS = InlineKeyboardButton('♉ Телец ♉', callback_data='zodiac')
BTN_HOROSCOPE_GEMINI = InlineKeyboardButton('♊ Близнецы ♊', callback_data='zodiac')
BTN_HOROSCOPE_CANCER = InlineKeyboardButton('♋ Рак ♋', callback_data='zodiac')
BTN_HOROSCOPE_LEO = InlineKeyboardButton('♌ Лев ♌', callback_data='zodiac')
BTN_HOROSCOPE_VIRGO = InlineKeyboardButton('♍ Дева ♍', callback_data='zodiac')
BTN_HOROSCOPE_LIBRA = InlineKeyboardButton('♎ Весы ♎', callback_data='zodiac')
BTN_HOROSCOPE_SCORPIO = InlineKeyboardButton('♏ Скорпион ♏', callback_data='zodiac')
BTN_HOROSCOPE_SAGITARIUS = InlineKeyboardButton('♐ Стрелец ♐', callback_data='zodiac')
BTN_HOROSCOPE_CAPRICORN = InlineKeyboardButton('♑ Козерог ♑', callback_data='zodiac')
BTN_HOROSCOPE_AQUARIUS = InlineKeyboardButton('♒ Водолей ♒', callback_data='zodiac')
BTN_HOROSCOPE_PISCES = InlineKeyboardButton('♓ Рыбы ♓', callback_data='zodiac')

# BTN_HOROSCOPE_ARIES = InlineKeyboardButton('♈ Овен ♈', callback_data='zodiac_aries')
# BTN_HOROSCOPE_TAURUS = InlineKeyboardButton('♉ Телец ♉', callback_data='zodiac_taurus')
# BTN_HOROSCOPE_GEMINI = InlineKeyboardButton('♊ Близнецы ♊', callback_data='zodiac_gemini')
# BTN_HOROSCOPE_CANCER = InlineKeyboardButton('♋ Рак ♋', callback_data='zodiac_canceler')
# BTN_HOROSCOPE_LEO = InlineKeyboardButton('♌ Лев ♌', callback_data='zodiac_leo')
# BTN_HOROSCOPE_VIRGO = InlineKeyboardButton('♍ Дева ♍', callback_data='zodiac_vigro')
# BTN_HOROSCOPE_LIBRA = InlineKeyboardButton('♎ Весы ♎', callback_data='zodiac_libra')
# BTN_HOROSCOPE_SCORPIO = InlineKeyboardButton('♏ Скорпион ♏', callback_data='zodiac_scorpio')
# BTN_HOROSCOPE_SAGITARIUS = InlineKeyboardButton('♐ Стрелец ♐', callback_data='zodiac_sagitarius')
# BTN_HOROSCOPE_CAPRICORN = InlineKeyboardButton('♑ Козерог ♑', callback_data='zodiac_capricorn')
# BTN_HOROSCOPE_AQUARIUS = InlineKeyboardButton('♒ Водолей ♒', callback_data='zodiac_aquarius')
# BTN_HOROSCOPE_PISCES = InlineKeyboardButton('♓ Рыбы ♓', callback_data='zodiac_pisces')

buttons_horoscope = [
    BTN_HOROSCOPE_ARIES, BTN_HOROSCOPE_TAURUS, BTN_HOROSCOPE_GEMINI,
    BTN_HOROSCOPE_CANCER, BTN_HOROSCOPE_LEO, BTN_HOROSCOPE_VIRGO, 
    BTN_HOROSCOPE_LIBRA, BTN_HOROSCOPE_SCORPIO, BTN_HOROSCOPE_SAGITARIUS,
    BTN_HOROSCOPE_CAPRICORN, BTN_HOROSCOPE_AQUARIUS, BTN_HOROSCOPE_PISCES
    ]

# for i in range(len(buttons_horoscope)):
#     keyboard_horoscope.insert(buttons_horoscope[i])
#     print(buttons_horoscope[i])
    
START_WEATHER = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(BTN_START_WEATHER)
WEATHER = InlineKeyboardMarkup().add(BTN_WIND, BTN_SUN_TIME)
WIND = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_SUN_TIME)
SUN_TIME = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND)
HELP = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_HOROSCOPE)
HOROSCOPE = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TODAY).add(BTN_HOROSCOPE_TOMORROW).add(BTN_HOROSCOPE_WEEK).add(BTN_HOROSCOPE_MONTH)
HOROSCOPE_TODAY = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TOMORROW).add(BTN_HOROSCOPE_WEEK).add(BTN_HOROSCOPE_MONTH)
HOROSCOPE_TOMORROW = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TODAY).add(BTN_HOROSCOPE_WEEK).add(BTN_HOROSCOPE_MONTH)
HOROSCOPE_WEEK = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TODAY).add(BTN_HOROSCOPE_TOMORROW).add(BTN_HOROSCOPE_MONTH)
HOROSCOPE_MONTH = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TODAY).add(BTN_HOROSCOPE_TOMORROW).add(BTN_HOROSCOPE_WEEK)
ZODIAC = InlineKeyboardMarkup(row_width=2).add(BTN_HOROSCOPE_ARIES, BTN_HOROSCOPE_TAURUS).add(BTN_HOROSCOPE_GEMINI, BTN_HOROSCOPE_CANCER).add(BTN_HOROSCOPE_LEO, BTN_HOROSCOPE_VIRGO).add(BTN_HOROSCOPE_LIBRA, BTN_HOROSCOPE_SCORPIO).add(BTN_HOROSCOPE_SAGITARIUS, BTN_HOROSCOPE_CAPRICORN).add(BTN_HOROSCOPE_AQUARIUS, BTN_HOROSCOPE_PISCES)

