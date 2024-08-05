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
    brand: Optional[str]
    condition: Optional[str]
    year: Optional[str]
    model: Optional[str]
    target: Optional[str]
    lifting_capacity: Optional[str]
    body_volume: Optional[str]
    number_of_axes: Optional[str]
    suspension_type: Optional[str]
    weight_without_load: Optional[str]
    axle_brand: Optional[str]
    type_of_brakes: Optional[str]
    ssu_height: Optional[str]
    internal_dimensions: Optional[str]
    phone: Optional[str]
    specifications_id: Optional[str]
    country: Optional[str]
    type_of_TS: Optional[str]
    engine_volume: Optional[str]
    type_of_fuel: Optional[str]
    image_id: Optional[int]
