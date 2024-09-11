from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.products.models import Products

from sqlalchemy import select


class NewsDAO(BaseDAO):
    model = Products
    
    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            
            return result
