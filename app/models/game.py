from sqlalchemy import BigInteger, UUID
from sqlalchemy.orm import Mapped, mapped_column
import uuid

from bd.db_manager import Base



class GameOrm(Base):
    __tablename__ = "games"


    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    name: Mapped[str]
    user_tg_id = mapped_column(BigInteger)