from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.main_content.models import MainContent
from app.main_content.schemas import SMainContent


class MainContentDAO(BaseDAO):
    model = MainContent
    
    @classmethod
    async def get_all(cls):
        query = (
            select(cls.model)
            .options(joinedload(cls.model.images))
        )
        async with async_session_maker() as session:
            result = await session.execute(query)
            main_content = result.scalars().unique().all()

            main_content_list: list = []
            for content in main_content:
                main_content_list.append(
                    SMainContent(
                        id=content.id,
                        logo=content.logo,
                        phone=content.phone,
                        email=content.email,
                        header_title=content.header_title,
                        header_desc=content.header_desc,
                        main_desc=content.main_desc,
                        products_title=content.products_title,
                        about_us_title=content.about_us_title,
                        images=[image.image_name for image in content.images],
                        about_us_desc=content.about_us_desc,
                        news_title=content.news_title,
                        brands_title=content.brands_title,
                        address=content.address,
                        link_to_the_map=content.link_to_the_map,
                    )
                )

            return main_content_list[0] if len(main_content) >= 1 else None  # only one record
