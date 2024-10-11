from typing import Optional, Annotated, List
from sqlalchemy import JSON, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType as _FileType
from typing import Any

from app.database import Base

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


class ImageType(_FileType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=FileSystemStorage(path='app/static/images'), *args, **kwargs)


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


class FileType(_FileType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=FileSystemStorage(path='app/files'), *args, **kwargs)


class PriceList(Base):
    __tablename__ = "price_lists"

    id: Mapped[intpk]
    file_name: Mapped[Optional[str]] = mapped_column(FileType())
    upload_data: Mapped[Optional[date]] = mapped_column(Date)
