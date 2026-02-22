from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Создать комнату", callback_data="create_game")],
    [KeyboardButton(text="Список комнат", callback_data="rooms_list")],
],
                        resize_keyboard=True,
)


async def inline_cars():
    # keyboard = ReplyKeyboardBuilder()
    data = []
    keyboard = InlineKeyboardBuilder()
    for item in data:
       keyboard.add(InlineKeyboardButton(text=item.name, url=""))
    return keyboard.adjust(2).as_markup()
