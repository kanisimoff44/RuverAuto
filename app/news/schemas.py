from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class SNewsAll(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]
    date_of_the_news: Optional[date]
    news_image_name: Optional[str]
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
