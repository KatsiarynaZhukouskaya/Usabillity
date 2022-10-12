from aiogram import Bot, Dispatcher, types, executor
from messages import start, weather, wind, sun_time, horoscope_today, horoscope_tomorrow, horoscope_week, horoscope_month
from inline_keyboard import ZODIAC, START, WEATHER, WIND, SUN_TIME, HELP, HOROSCOPE_TODAY, HOROSCOPE_TOMORROW, HOROSCOPE_WEEK, HOROSCOPE_MONTH, HOROSCOPE
from weatherData import Coordinates
from config import token

userCoordinates = {}


bot = Bot(token)
dp = Dispatcher(bot)

# обработка нажатий по инлайновым кнопакам
@dp.callback_query_handler(text='zodiac')
async def process_callback_zodiac(callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=horoscope_today()
        )
 
 
@dp.callback_query_handler(text='horoscope_today')
async def process_callback_horoscope_today(callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=horoscope_today(),
        reply_markup=HOROSCOPE_TODAY
        ) 
   
@dp.callback_query_handler(text='horoscope_tomorrow')
async def process_callback_horoscope_tomorrow(callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=horoscope_tomorrow(),
        reply_markup=HOROSCOPE_TOMORROW
        )
    
@dp.callback_query_handler(text='horoscope_week')
async def process_callback_horoscope_week(callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=horoscope_week(),
        reply_markup=HOROSCOPE_WEEK
        )
    
@dp.callback_query_handler(text='horoscope_month')
async def process_callback_horoscope_month(callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=horoscope_month(),
        reply_markup=HOROSCOPE_MONTH
        )
    
    
@dp.callback_query_handler(text='weather')
async def process_callback_weather(callback_query):
    await bot.answer_callback_query(callback_query.id)
    try:
        coord = userCoordinates[callback_query.from_user.id]
        await bot.send_message(callback_query.from_user.id,
                               text=weather(coord),
                               reply_markup=WEATHER)
    except:
        await bot.send_message(callback_query.from_user.id, text=start(), reply_markup=START)
    
@dp.callback_query_handler(text='wind')
async def process_callback_wind(callback_query):
    await bot.answer_callback_query(callback_query.id)
    try:
        coord = userCoordinates[callback_query.from_user.id]
        await bot.send_message(callback_query.from_user.id,
                               text=wind(coord),
                               reply_markup=WIND)   
    except:
        await bot.send_message(callback_query.from_user.id, text=start(), reply_markup=START)
    
@dp.callback_query_handler(text='sun_time')
async def process_callback_sun_time(callback_query):
    await bot.answer_callback_query(callback_query.id)
    try:
        coord = userCoordinates[callback_query.from_user.id]
        await bot.send_message(callback_query.from_user.id,
                               text=sun_time(coord),
                               reply_markup=SUN_TIME)   
    except:
        await bot.send_message(callback_query.from_user.id, text=start(), reply_markup=START)
    
    
# обработка команд

@dp.message_handler(commands=['horoscope_today'])
async def show_horoscope_today(message):
    await message.answer(text=horoscope_today(), reply_markup=HOROSCOPE_TODAY)
    
@dp.message_handler(commands=['horoscope_tomorrow'])
async def show_horoscope_tomorrow(message):
    await message.answer(text=horoscope_tomorrow(), reply_markup=HOROSCOPE_TOMORROW)
    
@dp.message_handler(commands=['horoscope_week'])
async def show_horoscope_week(message):
    await message.answer(text=horoscope_week(), reply_markup=HOROSCOPE_WEEK)

@dp.message_handler(commands=['horoscope_month'])
async def show_horoscope_month(message):
    await message.answer(text=horoscope_month(), reply_markup=HOROSCOPE_MONTH)

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    userCoordinates[message.from_user.id] = Coordinates(lat, lon)
    await message.answer("Great, now you can use all commands", reply_markup=HELP)
    

@dp.message_handler(commands=['start'])
async def show_start(message: types.Message):
    await message.answer(text=start(), reply_markup=START)
    
@dp.message_handler(commands=['weather'])
async def show_weather(message: types.Message):
    try:
        coord = userCoordinates[message.from_user.id]
        await message.answer(text=weather(coord), reply_markup=WEATHER)
    except:
        await message.answer(text=start(), reply_markup=START)
    
@dp.message_handler(commands=['wind'])
async def show_wind(message: types.Message):
    try:
        coord = userCoordinates[message.from_user.id]
        await message.answer(text=wind(coord), reply_markup=WIND)
    except:
        await message.answer(text=start(), reply_markup=START)

@dp.message_handler(commands=['sun_time'])
async def show_sun_time(message: types.Message):
    try:
        coord = userCoordinates[message.from_user.id]
        await message.answer(text=sun_time(coord), reply_markup=SUN_TIME)
    except:
        await message.answer(text=start(), reply_markup=START)
    
@dp.message_handler(commands=['help'])
async def show_help(message: types.Message):
    await message.answer(text="Choose one bot's commands", reply_markup=HELP)
    
@dp.message_handler(commands=['horoscope'])
async def show_horoscope(message):
    await message.answer(text=f"{message.from_user.first_name}, выберите желаемый гороскоп:", reply_markup=HOROSCOPE)


@dp.message_handler(commands=['zodiac'])
async def show_zodiac(message):
    await message.answer(text=f"{message.from_user.first_name}, выберите свой знак зодиака:", reply_markup=ZODIAC)


@dp.message_handler(commands=['hello'])
async def show_hello(message):
    send_mes = f"Hello, <b>{message.from_user.first_name}</b>! Have a good day!"
    await bot.send_message(message.chat.id, send_mes, parse_mode='html')


if __name__ == "__main__":
    executor.start_polling(dp)