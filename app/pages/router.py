from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.products.router import get_all_products, get_product_by_id
from app.products.schemas import SProductsAll, SProductsDetail

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates/")


@router.get("/main", response_class=HTMLResponse)
async def main_page(
    request: Request,
    products=Depends(get_all_products)
):
    """
    Main page
    """
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "products": products
        },
    )


@router.get("/products/{product_id}", response_class=HTMLResponse)
async def get_product_by_id(
    request: Request,
    product=Depends(get_product_by_id)
):
    return templates.TemplateResponse(
        "products.html",
        {
            "request": request,
            "product": product
        },
    )



# RuverAutu/
# ├── app/
# │   ├── main.py
# │   ├── database.py
# │   ├── config.py
# │   ├── products/
# │   │   ├── router.py
# │   │   └── models.py
# │   ├── templates/
# │   │   ├── base.html
# │   │   ├── index.html
# │   │   └── products.html
# │   ├── static/
# │   │   ├── css/
# │   │   │   └── style.css
# │   │   └── images/
# │   │       └── logo.png
# │   └── migrations/
# │       ├── versions/
# │       └── env.py
# ├── alembic.ini
# ├── requirements.txt
# ├── .env
# ├── .gitignore
# └── README.md