from typing import Optional, Annotated
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class Products(Base):
    __tablename__ = "products"
    
    id: Mapped[intpk]
    name: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    image_name: Mapped[Optional[str]]
    is_active: Mapped[bool]

    characteristics: Mapped[list["ProductsInfo"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )
    
    def __str__(self):
        return f"Товар: {self.name}"


class ProductsInfo(Base):
    __tablename__ = "products_info"

    id: Mapped[intpk]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    name_of_characteristic: Mapped[str]
    value_of_characteristic: Mapped[str]
    
    product: Mapped["Products"] = relationship(back_populates="characteristics")

    def __str__(self):
        return f"{self.name_of_characteristic}: {self.value_of_characteristic}"
