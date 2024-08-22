from typing import Annotated
from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str]
    hashed_password: Mapped[str]

    def __str__(self):
        return f"Пользователь {self.email}"
