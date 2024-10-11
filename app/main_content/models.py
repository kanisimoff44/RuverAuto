from typing import Optional, Annotated
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

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
    about_us_image: Mapped[Optional[str]]
    about_us_title: Mapped[Optional[str]]
    about_us_desc: Mapped[Optional[str]]
    news_title: Mapped[Optional[str]]
    brands_title: Mapped[Optional[str]]
    address: Mapped[Optional[str]]
    link_to_the_map: Mapped[Optional[str]]
    footer: Mapped[Optional[str]]

    def __str__(self):
        return f"Контент: {self.name}"
