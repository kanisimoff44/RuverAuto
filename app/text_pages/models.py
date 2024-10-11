from typing import Optional, Annotated
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class TextPages(Base):
    __tablename__ = "text_pages"

    id: Mapped[intpk]
    our_contacts: Mapped[Optional[str]]
    delivery_and_payment: Mapped[Optional[str]]
    privacy_policy: Mapped[Optional[str]]
    user_agreement: Mapped[Optional[str]]

    def __str__(self):
        return f"Страница: {self.name}"
