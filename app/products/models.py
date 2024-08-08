from typing import Optional, Annotated
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class Products(Base):
    __tablename__ = "products"
    
    id: Mapped[intpk]
    name: Mapped[str]
    description: Mapped[Optional[str]]
    image_name: Mapped[str]
    is_active: Mapped[bool]

    characteristics: Mapped[list["ProductsInfo"]] = relationship(back_populates="product")


class ProductsInfo(Base):
    __tablename__ = "products_info"

    id: Mapped[intpk]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    name_of_characteristic: Mapped[str]
    value_of_characteristic: Mapped[str]
    
    product: Mapped["Products"] = relationship(back_populates="characteristics")
