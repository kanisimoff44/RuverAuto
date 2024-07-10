from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates/")


@router.get("/main", response_class=HTMLResponse)
async def main_page(request: Request):
    """
    Main page
    """
    return templates.TemplateResponse("main.html", {"request": request})


@router.get("/products", response_class=HTMLResponse)
async def read_products(request: Request):
    """
    Get all products

    Returns:
        list[Products]: list of products
    """
    return templates.TemplateResponse("products.html", {"request": request, "products": []})
