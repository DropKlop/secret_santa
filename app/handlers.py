from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app.keyboards import main, inline_cars
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.middleware import AnyTextMiddleware


router = Router()

router.message.outer_middleware(AnyTextMiddleware())


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name} \nВыберите команду', reply_markup=main)


@router.callback_query(F.data=='create_game')
async def cmd_create(msg: Message):
    pass


@router.callback_query(F.data=='rooms_list?')
async def cmd_rooms_list(msg: Message):
    pass


@router.callback_query(F.data=="catalog")# для отработки callback_data у inline кнопок
async def catalog(callback: CallbackQuery):
    await callback.answer('Выбран каталог')
    await callback.message.edit_text('Ку', reply_markup=await inline_cars())# заменить текст на указанный тут и заменит кнопки на кнопки из функции
