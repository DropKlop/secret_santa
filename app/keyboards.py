from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Создать комнату", callback_data="create_game")],
    [InlineKeyboardButton(text="Список комнат", callback_data="rooms_list")],
])


#settings = InlineKeyboardMarkup(inline_keyboard=[
#    [InlineKeyboardButton(text='Пук', url='https://kwork.ru/user/sadfrog')]
#])


cars = ['Tesla', 'Mercedes', 'Audi']

async def inline_cars():
    # keyboard = ReplyKeyboardBuilder()
    keyboard = InlineKeyboardBuilder()
    for car in cars:
       # keyboard.add(KeyboardButton(text=car))
       keyboard.add(InlineKeyboardButton(text=car, url="https://kwork.ru/user/sadfrog"))
    return keyboard.adjust(2).as_markup()
