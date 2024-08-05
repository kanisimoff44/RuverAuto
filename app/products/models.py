from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Products(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    brand: Mapped[Optional[str]]
    condition: Mapped[Optional[str]]
    year: Mapped[Optional[str]]
    model: Mapped[Optional[str]]
    target: Mapped[Optional[str]]
    lifting_capacity: Mapped[Optional[str]]
    body_volume: Mapped[Optional[str]]
    number_of_axes: Mapped[Optional[str]]
    suspension_type: Mapped[Optional[str]]
    weight_without_load: Mapped[Optional[str]]
    axle_brand: Mapped[Optional[str]]
    type_of_brakes: Mapped[Optional[str]]
    ssu_height: Mapped[Optional[str]]
    internal_dimensions: Mapped[Optional[str]]
    phone: Mapped[Optional[str]]
    specifications_id: Mapped[Optional[str]]
    country: Mapped[Optional[str]]
    type_of_TS: Mapped[Optional[str]]
    engine_volume: Mapped[Optional[str]]
    type_of_fuel: Mapped[Optional[str]]
    image_id: Mapped[int]
