from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SNewsDetail(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]
    date_of_the_news: Optional[str]
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class SNewsAll(SNewsDetail):
    short_description: Optional[str]
    date_of_the_news: Optional[date]
    images: Optional[list]
