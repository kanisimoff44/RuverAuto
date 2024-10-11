from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.products.dao import PriceListDAO
from app.products.router import get_all_products, get_product_by_id, get_price_list
from app.main_content.router import get_content
from app.news.router import get_all_news, get_news_by_id
from app.text_pages.router import get_text_page


router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates/")


@router.get("/main", response_class=HTMLResponse)
async def main_page(
    request: Request,
    products=Depends(get_all_products),
    content=Depends(get_content),
    all_news=Depends(get_all_news),
    page=Depends(get_text_page)
):
    """
    Main page
    """
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "products": products,
            "content": content,
            "all_news": all_news,
            "page": page
        },
    )


@router.get("/products", response_class=HTMLResponse)
async def get_all_product(
    request: Request,
    products=Depends(get_all_products),
    all_news=Depends(get_all_news),
    content=Depends(get_content),
    page=Depends(get_text_page)
):
    price_list = await PriceListDAO.get_price_list()

    return templates.TemplateResponse(
        "products.html",
        {
            "request": request,
            "products": products,
            "all_news": all_news,
            "content": content,
            "price_list": price_list[-1],  # get last price-list if more than one
            "page": page
        },
    )


@router.get("/products/{product_id}", response_class=HTMLResponse)
async def get_product_by_id(
    request: Request,
    products=Depends(get_all_products),
    product=Depends(get_product_by_id),
    all_news=Depends(get_all_news),
    content=Depends(get_content),
    page=Depends(get_text_page)
):

    
    return templates.TemplateResponse(
        "product_detail.html",
        {
            "request": request,
            "products": products,
            "product": product,
            "all_news": all_news,
            "content": content,
            "page": page
        },
    )


@router.get("/news", response_class=HTMLResponse)
async def get_all_news(
    request: Request,
    products=Depends(get_all_products),
    all_news=Depends(get_all_news),
    content=Depends(get_content),
    page=Depends(get_text_page)
):
    return templates.TemplateResponse(
        "news.html",
        {
            "request": request,
            "products": products,
            "all_news": all_news,
            "content": content,
            "page": page
        },
    )

@router.get("/news/{news_id}", response_class=HTMLResponse)
async def get_news_by_id(
    request: Request,
    products=Depends(get_all_products),
    all_news=Depends(get_all_news),
    news=Depends(get_news_by_id),
    content=Depends(get_content),
    page=Depends(get_text_page)
):
    return templates.TemplateResponse(
        "news_detail.html",
        {
            "request": request,
            "products": products,
            "all_news": all_news,
            "news": news,
            "content": content,
            "page": page
        },
    )


@router.get("/delivery-and-payment", response_class=HTMLResponse)
async def delivery_and_payment(
    request: Request,
    products=Depends(get_all_products),
    all_news=Depends(get_all_news),
    content=Depends(get_content),
    page=Depends(get_text_page)
):
    return templates.TemplateResponse(
        "delivery_and_payment.html",
        {
            "request": request,
            "products": products,
            "all_news": all_news,
            "content": content,
            "page": page
        },
    )


@router.get("/our-contacts", response_class=HTMLResponse)
async def our_contacts(
    request: Request,
    products=Depends(get_all_products),
    all_news=Depends(get_all_news),
    content=Depends(get_content),
    page=Depends(get_text_page)
):
    return templates.TemplateResponse(
        "our_contacts.html",
        {
            "request": request,
            "products": products,
            "all_news": all_news,
            "content": content,
            "page": page
        },
    )


@router.get("/privacy-policy", response_class=HTMLResponse)
async def privacy_policy(
    request: Request,
    products=Depends(get_all_products),
    all_news=Depends(get_all_news),
    content=Depends(get_content),
    page=Depends(get_text_page)
):
    return templates.TemplateResponse(
        "privacy_policy.html",
        {
            "request": request,
            "products": products,
            "all_news": all_news,
            "content": content,
            "page": page
        },
    )


@router.get("/user-agreement", response_class=HTMLResponse)
async def user_agreement(
    request: Request,
    products=Depends(get_all_products),
    all_news=Depends(get_all_news),
    content=Depends(get_content),
    page=Depends(get_text_page)
):
    return templates.TemplateResponse(
        "user_agreement.html",
        {
            "request": request,
            "products": products,
            "all_news": all_news,
            "content": content,
            "page": page
        },
    )