from fastapi import APIRouter
from fastapi.responses import FileResponse
# from fastapi_cache.decorator import cache

from app.products.dao import ProductsDAO, PriceListDAO
from app.products.schemas import SProductsAll, SProductsDetail
from app.utils import check_product_img
from fastapi.responses import RedirectResponse

router = APIRouter(
    prefix="/products",
    tags=["Товары"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_products() -> list[SProductsAll]:
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    products = await ProductsDAO.get_all()
    for product in products:
        check_product_img(product)

    return products


@router.get("/{product_id}")
# @cache(expire=3600)
async def get_product_by_id(product_id: int) -> SProductsDetail:
    """
    Get product by id

    Args:
        product_id (int): _description_

    Returns:
        SProductDetail: _description_
    """
    product = await ProductsDAO.get_by_id(product_id)
    print(product)
    # check_product_img(product)

    return product


@router.get("/download/{file_id}")
async def get_price_list():
    price_list = await PriceListDAO.get_price_list()

    file_path = price_list[-1].file_name

    if not file_path:
        return RedirectResponse("/pages/products")

    return FileResponse(
        path=file_path,
        filename="price_list.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
