from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.products.models import Products, PriceList
from app.products.schemas import SProductsAll

from sqlalchemy import select
from sqlalchemy.orm import joinedload


class ProductsDAO(BaseDAO):
    model = Products
    
    @classmethod
    async def get_all(cls):
        get_products_with_info = (
            select(cls.model)
            .options(joinedload(cls.model.images))
            .options(joinedload(cls.model.characteristics, innerjoin=False))
        )
        async with async_session_maker() as session:
            result = await session.execute(get_products_with_info)
            products = result.unique().scalars().all()

            products_list: list = []
            for product in products:
                short_description = ""
                if product.description:
                    short_description = (
                        product.description[:50] + '...'
                        if len(product.description) > 50
                        else product.description[:50]
                    )
                products_list.append(
                    SProductsAll(
                        id=product.id,
                        name=product.name,
                        description=product.description,
                        short_description=short_description,
                        images=[image.image_name for image in product.images],
                        price=product.price,
                        label=product.label,
                        is_active=product.is_active,
                        characteristics=[
                            {"name": char.name_of_characteristic, "value": char.value_of_characteristic}
                            for char in product.characteristics
                        ]
                    )
                )
            return products_list

    @classmethod
    async def get_by_id(cls, product_id: int):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .options(joinedload(cls.model.images))
                .options(joinedload(cls.model.characteristics))
                .filter_by(id=product_id)
            )
            result = await session.execute(query)
            product = result.unique().scalar_one_or_none()

            return product


class PriceListDAO(BaseDAO):
    model = PriceList

    @classmethod
    async def get_price_list(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            price_list = await session.execute(query)
            return price_list.scalars().all()
