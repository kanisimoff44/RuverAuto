from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Авто"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_products():
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    return {"message": "Список автомобилей"}
