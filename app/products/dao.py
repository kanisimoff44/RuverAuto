from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.products.models import Products
from app.products.schemas import SProductsInfo

from sqlalchemy import select


class ProductsDAO(BaseDAO):
    model = Products
    
    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return [
                SProductsInfo(
                    id=product.id,
                    name=product.name,
                    description=product.description,
                    short_description=product.description[:50] + '...',
                    image_id=product.image_id
                ) for product in result
            ]

    @classmethod
    async def get_by_id(cls, product_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=product_id)
            product = await session.execute(query)
            return product.scalar_one_or_none()
