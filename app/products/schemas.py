from pydantic import BaseModel, ConfigDict
from typing import Optional


class SProductsDetail(BaseModel):
    id: int
    name: str
    description: Optional[str]
    image_name: str | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class SProductsAll(SProductsDetail):
    short_description: Optional[str]
