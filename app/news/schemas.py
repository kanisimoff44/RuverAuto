from pydantic import BaseModel, ConfigDict
from typing import Optional


class SNewsAll(BaseModel):
    id: int
    name: str
    description: Optional[str]
    date_of_the_news: str | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
