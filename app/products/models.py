from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Products(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    image_id: Mapped[int]
