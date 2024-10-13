from datetime import date
from typing import Annotated, Optional

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.utils import ImageType

intpk = Annotated[int, mapped_column(primary_key=True)]


class News(Base):
    __tablename__ = "news"
    
    id: Mapped[intpk]
    title: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    date_of_the_news: Mapped[Optional[date]] = mapped_column(Date)
    is_active: Mapped[bool]
    
    images: Mapped[list["NewsImages"]] = relationship(
        back_populates="the_news",
        cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Новость: {self.title}"


class NewsImages(Base):
    __tablename__ = "news_images"

    id: Mapped[intpk]
    news_id: Mapped[int] = mapped_column(ForeignKey("news.id", ondelete="CASCADE"))
    news_image_name: Mapped[Optional[str]] = mapped_column(ImageType())

    the_news: Mapped["News"] = relationship(back_populates="images")

    def __str__(self):
        return f"Изображение: {self.news_image_name.split('/')[-1]}"
