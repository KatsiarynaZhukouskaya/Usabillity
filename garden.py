from models import January, February, March, April, May, June, July, August, September, October, November, December
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from models import db


month = [January, February, March, April, May, 
         June, July, August, September, 
         October, November, December]

keyboard_sets = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)

BTN_January = InlineKeyboardButton(text="Январь")
BTN_February = InlineKeyboardButton(text="Февраль")
BTN_March = InlineKeyboardButton(text="Март")
BTN_April = InlineKeyboardButton(text="Апрель")
BTN_May = InlineKeyboardButton(text="Май")
BTN_June = InlineKeyboardButton(text="Июнь")
BTN_July = InlineKeyboardButton(text="Июль")
BTN_August = InlineKeyboardButton(text="Август")
BTN_September = InlineKeyboardButton(text="Сентябрь")
BTN_October = InlineKeyboardButton(text="Октябрь")
BTN_November = InlineKeyboardButton(text="Ноябрь")
BTN_December = InlineKeyboardButton(text="Декабрь")

buttons = [BTN_January, BTN_February, BTN_March, BTN_April, BTN_May, BTN_June, 
           BTN_July, BTN_August, BTN_September, BTN_October, BTN_November, BTN_December]

for i in range(len(buttons)):
    keyboard_sets.insert(buttons[i])


def get_keybord(month):
    """Возвращает inline-клавиатуру с кнопками, после нажатия на которые выдает необходимый совет"""
    with db:
        advice = month.select()
        advice_keybord = InlineKeyboardMarkup(row_width=2)
        btn_advice = f"{advice[i].name} ({advice[i].description})"
        advice_keybord.insert(btn_advice)
    return advice_keybord


