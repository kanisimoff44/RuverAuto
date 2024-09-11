from typing import Optional, Annotated
from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from app.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class News(Base):
    __tablename__ = "news"
    
    id: Mapped[intpk]
    title: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    date_of_the_news: Mapped[Optional[date]] = mapped_column(Date)
    news_image_name: Mapped[Optional[str]]
    is_active: Mapped[bool]

    def __str__(self):
        return f"Новость: {self.name}"
