from datetime import date
from typing import Annotated, Optional

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.utils import FileType, ImageType

intpk = Annotated[int, mapped_column(primary_key=True)]


class Products(Base):
    __tablename__ = "products"

    id: Mapped[intpk]
    name: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    price: Mapped[Optional[int]]
    label: Mapped[Optional[bool]]
    is_active: Mapped[bool]

    characteristics: Mapped[list["ProductsInfo"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )

    images: Mapped[list["ProductsImages"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Товар: {self.name}"


class ProductsImages(Base):
    __tablename__ = "products_images"

    id: Mapped[intpk]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    image_name: Mapped[Optional[str]] = mapped_column(ImageType())

    product: Mapped["Products"] = relationship(back_populates="images")

    def __str__(self):
        return f"Изображение: {self.image_name.split('/')[-1]}"


class ProductsInfo(Base):
    __tablename__ = "products_info"

    id: Mapped[intpk]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    name_of_characteristic: Mapped[str]
    value_of_characteristic: Mapped[str]
    
    product: Mapped["Products"] = relationship(back_populates="characteristics")

    def __str__(self):
        return f"{self.name_of_characteristic}: {self.value_of_characteristic}"


class PriceList(Base):
    __tablename__ = "price_lists"

    id: Mapped[intpk]
    file_name: Mapped[Optional[str]] = mapped_column(FileType())
    upload_data: Mapped[Optional[date]] = mapped_column(Date)
