from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_builder = ReplyKeyboardBuilder()

# Функционал к команде "Давай"
paper_btn = KeyboardButton(text='📜Бумага')
rock_btn = KeyboardButton(text='🌑Камень')
scissors = KeyboardButton(text='✂️Ножницы')

kb_builder.row(paper_btn, rock_btn, scissors, width=1)
rock_paper_scissors_keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True)

# функционал к команде "/start"
StartKeyboard = ReplyKeyboardBuilder()

i_want_btn = KeyboardButton(text='Давай!')
no_btn = KeyboardButton(text='Не хочу!')

StartKeyboard.row(i_want_btn, no_btn, width=2)
start_keyboard: ReplyKeyboardMarkup = StartKeyboard.as_markup(
    resize_keyboard=True)
