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
async def cmd_create(callback: CallbackQuery):
    await callback.answer('Создание комнаты')
    await callback.message.reply('')


@router.callback_query(F.data=='rooms_list')
async def cmd_rooms_list(callback: CallbackQuery):
    pass
