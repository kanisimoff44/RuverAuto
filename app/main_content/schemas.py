from pydantic import BaseModel, ConfigDict


class SMainContent(BaseModel):
    logo: str | None
    phone: str | None
    email: str | None
    main_urls: str | None
    main_title: str | None
    main_desc: str | None
    products_title: str | None
    product_title: str | None
    footer: str | None

    model_config = ConfigDict(from_attributes=True)
