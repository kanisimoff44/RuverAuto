from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.news.models import News
from app.news.schemas import SNewsAll

from sqlalchemy import select


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
