from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

BTN_START = KeyboardButton('Send my location🗺',
                           request_location=True,
                           resize_keyboard=True,
                           one_time_keyboard=True)
BTN_WEATHER = InlineKeyboardButton('🌦Weather❄️', callback_data='weather')
BTN_WIND = InlineKeyboardButton('💨Wind💨', callback_data='wind')
BTN_SUN_TIME = InlineKeyboardButton('Sunrise☀️ and sunset🌙', callback_data='sun_time')
BTN_HOROSCOPE = InlineKeyboardButton("Выберите гороскоп")
BTN_HOROSCOPE_TODAY = InlineKeyboardButton('Гороскоп на сегодня:', callback_data='horoscope_today')
BTN_HOROSCOPE_TOMORROW = InlineKeyboardButton('Гороскоп на завтра:', callback_data='horoscope_tomorrow')
BTN_HOROSCOPE_WEEK = InlineKeyboardButton('Гороскоп на неделю:', callback_data='horoscope_week')
BTN_HOROSCOPE_MONTH = InlineKeyboardButton('Гороскоп на месяц:', callback_data='horoscope_month')


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



START = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(BTN_START)
WEATHER = InlineKeyboardMarkup().add(BTN_WIND, BTN_SUN_TIME)
WIND = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_SUN_TIME)
SUN_TIME = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND)
HELP = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND).add(BTN_SUN_TIME)
HOROSCOPE = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TODAY).add(BTN_HOROSCOPE_TOMORROW).add(BTN_HOROSCOPE_WEEK).add(BTN_HOROSCOPE_MONTH)
HOROSCOPE_TODAY = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TOMORROW).add(BTN_HOROSCOPE_WEEK).add(BTN_HOROSCOPE_MONTH)
HOROSCOPE_TOMORROW = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TODAY).add(BTN_HOROSCOPE_WEEK).add(BTN_HOROSCOPE_MONTH)
HOROSCOPE_WEEK = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TODAY).add(BTN_HOROSCOPE_TOMORROW).add(BTN_HOROSCOPE_MONTH)
HOROSCOPE_MONTH = InlineKeyboardMarkup().add(BTN_HOROSCOPE_TODAY).add(BTN_HOROSCOPE_TOMORROW).add(BTN_HOROSCOPE_WEEK)


ZODIAC = InlineKeyboardMarkup(row_width=2).add(BTN_HOROSCOPE_ARIES, BTN_HOROSCOPE_TAURUS).add(BTN_HOROSCOPE_GEMINI, BTN_HOROSCOPE_CANCER).add(BTN_HOROSCOPE_LEO, BTN_HOROSCOPE_VIRGO).add(BTN_HOROSCOPE_LIBRA, BTN_HOROSCOPE_SCORPIO).add(BTN_HOROSCOPE_SAGITARIUS, BTN_HOROSCOPE_CAPRICORN).add(BTN_HOROSCOPE_AQUARIUS, BTN_HOROSCOPE_PISCES)