from sqlalchemy import Enum
from typing import Annotated
from sqlalchemy.orm import mapped_column, Mapped
from enum import Enum as PyEnum

from app.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class Roles(PyEnum):
    ROOT = "root"
    ADMIN = "admin"
    USER = "user"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str]
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    role: Mapped[Roles] = mapped_column(Enum(Roles), default=Roles.USER)

    def __str__(self):
        return f"Пользователь {self.email}"
