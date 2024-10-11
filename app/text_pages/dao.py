from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.text_pages.models import TextPages

from sqlalchemy import select


class TextPagesDAO(BaseDAO):
    model = TextPages
    
    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)

            return result.scalar_one_or_none()
