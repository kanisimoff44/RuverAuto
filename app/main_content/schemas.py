from typing import Optional

from pydantic import BaseModel, ConfigDict


class SMainContent(BaseModel):
    id: int
    logo: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    header_title: Optional[str]
    header_desc: Optional[str]
    main_desc: Optional[str]
    products_title: Optional[str]
    about_us_title: Optional[str]
    images: Optional[list]
    about_us_desc: Optional[str]
    news_title: Optional[str]
    brands_title: Optional[str]
    address: Optional[str]
    link_to_the_map: Optional[str]

    model_config = ConfigDict(from_attributes=True)
