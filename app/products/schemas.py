from pydantic import BaseModel, ConfigDict
from typing import Optional


class SProducts(BaseModel):
    id: int
    name: str
    description: Optional[str]
    short_description: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class SProductsInfo(SProducts):
    image_id: int


class SProductDetail(BaseModel):
    id: int
    name: str
    description: Optional[str]
    image_id: int
