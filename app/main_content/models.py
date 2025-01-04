from typing import Annotated, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.utils import ImageType

intpk = Annotated[int, mapped_column(primary_key=True)]


class MainContent(Base):
    __tablename__ = "main_content"
    
    id: Mapped[intpk]
    logo: Mapped[Optional[str]]
    phone: Mapped[Optional[str]]
    email: Mapped[Optional[str]]
    header_title: Mapped[Optional[str]]
    header_desc: Mapped[Optional[str]]
    main_desc: Mapped[Optional[str]]
    products_title: Mapped[Optional[str]]
    about_us_title: Mapped[Optional[str]]
    about_us_desc: Mapped[Optional[str]]
    news_title: Mapped[Optional[str]]
    brands_title: Mapped[Optional[str]]
    address: Mapped[Optional[str]]
    link_to_the_map: Mapped[Optional[str]]

    images: Mapped[list["AboutUsImages"]] = relationship(
        back_populates="about_us",
        cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Контент: {self.about_us_title}"


class AboutUsImages(Base):
    __tablename__ = "about_us_images"

    id: Mapped[intpk]
    about_us_id: Mapped[int] = mapped_column(ForeignKey("main_content.id", ondelete="CASCADE"))
    image_name: Mapped[Optional[str]] = mapped_column(ImageType())

    about_us: Mapped["MainContent"] = relationship(back_populates="images")

    def __str__(self):
        return f"Изображение: {self.image_name.split('/')[-1]}"
