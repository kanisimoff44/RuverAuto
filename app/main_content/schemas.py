from pydantic import BaseModel, ConfigDict


class SMainContent(BaseModel):
    logo: str | None
    phone: str | None
    email: str | None
    header_title: str | None
    header_desc: str | None
    main_desc: str | None
    products_title: str | None
    about_us_image: str | None
    about_us_title: str | None
    about_us_desc: str | None
    news_title: str | None
    brands_title: str | None
    link_to_the_map: str | None
    footer: str | None

    model_config = ConfigDict(from_attributes=True)
