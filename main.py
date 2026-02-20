import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import settings
from app.handlers import router as main_router



bot = Bot(token=settings.BOT_TOKEN)
db = Dispatcher()


async def main():
    db.include_router(main_router)
    await db.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
