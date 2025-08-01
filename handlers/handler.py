from lexicon.lexicon import lexicon_for_bot
from keyboard.keyboard import start_keyboard, rock_paper_scissors_keyboard
from random import choice

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram import F, Bot
from aiogram.types import Message

router = Router()

rock_paper_scissors_list = ['✂️Ножницы', '🌑Камень', '📜Бумага']


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(text=lexicon_for_bot['start'], reply_markup=start_keyboard)


@router.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer(text=lexicon_for_bot['help'])


@router.message(F.text == 'Давай!')
async def davai_cmd(message: Message):
    await message.answer(text='Отлично! Делай свой выбор!', reply_markup=rock_paper_scissors_keyboard)


@router.message(F.text == 'Не хочу!')
async def ne_davai_cmd(message: Message):
    await message.answer(text='Хорошо, если передумаешь, то пиши команду /start')


@router.message(F.text.in_(['✂️Ножницы', '🌑Камень', '📜Бумага']))
async def main_handler(message: Message):
    random_rock_paper_scissors = choice(rock_paper_scissors_list)
    if message.text == random_rock_paper_scissors:
        await message.answer(random_rock_paper_scissors)
        await message.answer('Ой, давай попробуем снова?')
    elif message.text == '📜Бумага' and random_rock_paper_scissors == '✂️Ножницы':
        await message.answer(random_rock_paper_scissors)
        await message.answer('Ты проиграл. Давай попробуем снова?', reply_markup=start_keyboard)
    elif message.text == '🌑Камень' and random_rock_paper_scissors == '📜Бумага':
        await message.answer(random_rock_paper_scissors)
        await message.answer('Ты проиграл. Давай попробуем снова?', reply_markup=start_keyboard)
    elif message.text == '✂️Ножницы' and random_rock_paper_scissors == '🌑Камень':
        await message.answer(random_rock_paper_scissors)
        await message.answer('Ты проиграл. Давай попробуем снова?', reply_markup=start_keyboard)
    elif message.text == '✂️Ножницы' and random_rock_paper_scissors == '🌑Камень':
        await message.answer(random_rock_paper_scissors)
        await message.answer('Ты проиграл. Давай попробуем снова?', reply_markup=start_keyboard)
    else:
        await message.answer(random_rock_paper_scissors)
        await message.answer('Ты победил. Давай попробуем снова?', reply_markup=start_keyboard)
