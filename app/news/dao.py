from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.news.models import News
from app.news.schemas import SNewsAll

from sqlalchemy import select
from sqlalchemy.orm import joinedload


class NewsDAO(BaseDAO):
    model = News
    
    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.c)
            all_news = await session.execute(query)

            news_list: list = []
            for news in all_news:
                short_description = ""
                if news.description:
                        short_description = (
                            news.description[:50] + '...' 
                            if len(news.description) > 50 
                            else news.description[:50]
                        )
                news_list.append(
                    SNewsAll(
                        id=news.id,
                        title=news.title,
                        description=news.description,
                        short_description=short_description,
                        date_of_the_news=news.date_of_the_news,
                        news_image_name=news.news_image_name,
                        is_active=news.is_active,
                    )
                )
            return news_list

    @classmethod
    async def get_by_id(cls, news_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=news_id)
            result = await session.execute(query)
            news = result.unique().scalar_one_or_none()

            return news
