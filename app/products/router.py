from fastapi import APIRouter

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
    return products


@router.get("/{product_id}")
async def get_product_by_id(product_id: int) -> SProductDetail:
    """
    Get product by id

    Args:
        product_id (int): _description_

    Returns:
        SProductsInfo: _description_
    """
    product = await ProductsDAO.get_by_id(product_id)
    return product
