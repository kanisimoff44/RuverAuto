from typing import Optional

from pydantic import BaseModel, ConfigDict


class SProductsDetail(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: Optional[int]
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class SProductsAll(SProductsDetail):
    label: Optional[bool]
    short_description: Optional[str]
    characteristics: Optional[list]
    images: Optional[list]
