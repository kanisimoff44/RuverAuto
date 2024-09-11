from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.news.models import News

from sqlalchemy import select


class NewsDAO(BaseDAO):
    model = News
    
    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.c)
            result = await session.execute(query)
            return result.mappings().all()
