import os
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.products.dao import ProductsDAO
from app.products.schemas import SProductsInfo, SProductDetail

router = APIRouter(
    prefix="/products",
    tags=["Товары"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_products() -> list[SProductsInfo]:
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    products = await ProductsDAO.get_all()
    
    image_directory = "app/static/images/"
    
    for product in products:
        if not os.path.exists(f"{image_directory}{product.image_id}.webp"):
            product.image_id = None
    
    return products


@router.get("/{product_id}")
@cache(expire=3600)
async def get_product_by_id(product_id: int) -> SProductDetail:
    """
    Get product by id

    Args:
        product_id (int): _description_

    Returns:
        SProductsInfo: _description_
    """
    product = await ProductsDAO.get_by_id(product_id)
    
    image_directory = "app/static/images/"
    if not os.path.exists(f"{image_directory}{product.image_id}.webp"):
        product.image_id = None
    
    return product
