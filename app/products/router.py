import os
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.products.dao import ProductsDAO
from app.products.schemas import SProductsInfo
from app.products.labels import column_labels

router = APIRouter(
    prefix="/products",
    tags=["Товары"],
    responses={404: {"description": "Not found"}},
)

def check_img(product: SProductsInfo):
    image_directory = "app/static/images/"
    if not os.path.exists(f"{image_directory}{product.image_name}.webp"):
        product.image_name = None
    
    return product.image_name


@router.get("/")
async def get_all_products() -> list[SProductsInfo]:
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    products = await ProductsDAO.get_all()

    for product in products:
        check_img(product)
    
    return products


@router.get("/{product_id}")
# @cache(expire=3600)
async def get_product_by_id(product_id: int) -> SProductsInfo:
    """
    Get product by id

    Args:
        product_id (int): _description_

    Returns:
        SProductDetail: _description_
    """
    product = await ProductsDAO.get_by_id(product_id)
    check_img(product)
    
    return product
