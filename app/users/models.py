from enum import Enum as PyEnum
from typing import Annotated

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class Roles(PyEnum):
    ROOT = "root"
    ADMIN = "admin"
    USER = "user"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str]
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    role: Mapped[Roles] = mapped_column(Enum(Roles), default=Roles.USER)

    def __str__(self):
        return f"Пользователь {self.username}"
