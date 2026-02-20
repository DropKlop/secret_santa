from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Any, Awaitable, Dict



class AnyTextMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        text_from_msg = event.model_dump()['text']
        print(f"Действие до {text_from_msg}")
        res = await handler(event, data)
        print("Действие после")
        return res
