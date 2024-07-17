from pydantic import BaseModel, ConfigDict
from typing import Optional


class SProducts(BaseModel):
    id: int
    name: str
    description: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class SProductsInfo(SProducts):
    short_description: Optional[str]
    image_id: int


class SProductDetail(BaseModel):
    id: int
    name: str
    description: Optional[str]
    image_id: int
