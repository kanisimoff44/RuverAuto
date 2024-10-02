import os

from app.products.schemas import SProductsDetail
from app.news.schemas import SNewsDetail


def check_product_img(product: SProductsDetail) -> str:
    image_directory = "app/static/images/"
    if not os.path.exists(f"{image_directory}{product.image_name}"):
        product.image_name = None
    
    return product.image_name


def check_news_img(news: SNewsDetail) -> str:
    image_directory = "app/static/images/"
    if not os.path.exists(f"{image_directory}{news.news_image_name}"):
        news.image_name = None
    
    return news.news_image_name
