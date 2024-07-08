from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates/")


@router.get("/products")
async def read_products():
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    return templates.TemplateResponse("index.html", {"request": {}, "products": []})
