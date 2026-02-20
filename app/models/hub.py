from sqlalchemy import BigInteger, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column
import uuid

from bd.db_manager import Base



class HubOrm(Base):
    __tablename__ = "hubs"


    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id_tg = mapped_column(BigInteger)
    game_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey("games.id"))