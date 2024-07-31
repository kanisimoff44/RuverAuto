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
            products: list = []
            for product in result:
                short_description: str = "Нет описания"
                if product.description:
                    short_description = product.description[:50] + '...'
                products.append(
                    SProductsInfo(
                        id=product.id,
                        name=product.name,
                        description=product.description,
                        short_description=short_description,
                        image_id=product.image_id
                    )
                )
            return products

    @classmethod
    async def get_by_id(cls, product_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=product_id)
            product = await session.execute(query)
            return product.scalar_one_or_none()
