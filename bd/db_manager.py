from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings

engine = create_async_engine(settings.db_url)
session_async = async_sessionmaker(engine)

# для создания моделей бд
class Base(DeclarativeBase):
    pass