from models import January, February, March, April, May, June, July,\
                    August, September, October, November, December, db
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,\
                    InlineKeyboardButton, InlineKeyboardMarkup


keyboard_sets = ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)

BTN_January = KeyboardButton(text="Январь")
BTN_February = KeyboardButton(text="Февраль")
BTN_March = KeyboardButton(text="Март")
BTN_April = KeyboardButton(text="Апрель")
BTN_May = KeyboardButton(text="Май")
BTN_June = KeyboardButton(text="Июнь")
BTN_July = KeyboardButton(text="Июль")
BTN_August = KeyboardButton(text="Август")
BTN_September = KeyboardButton(text="Сентябрь")
BTN_October = KeyboardButton(text="Октябрь")
BTN_November = KeyboardButton(text="Ноябрь")
BTN_December = KeyboardButton(text="Декабрь")

month = [January, February, March, April, May, 
         June, July, August, September, 
         October, November, December]

buttons = [BTN_January, BTN_February, BTN_March, BTN_April, BTN_May, BTN_June, 
           BTN_July, BTN_August, BTN_September, BTN_October, BTN_November, BTN_December]

for i in range(len(buttons)):
    keyboard_sets.insert(buttons[i])
    
    
def get_keyboard(model):
    
    with db:
        advice = model.select()
        advice_keyboard = InlineKeyboardMarkup(row_width=1)
        for i in range(len(advice)):
            btn_advice = InlineKeyboardButton(text=f"{advice[i].description}", url='https://www.youtube.com/c/%D0%A1%D0%B0%D0%B4%D0%BE%D0%B2%D1%8B%D0%B9%D0%93%D0%B8%D0%B4')
            advice_keyboard.insert(btn_advice)
    return advice_keyboard

