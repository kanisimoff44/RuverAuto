import os

from app.products.schemas import SProductsDetail
from app.news.schemas import SNewsDetail


def check_product_img(product: SProductsDetail) -> str:
    names_images = []
    if len(product.images) == 0:
        product.images = None
    else:
        for image in product.images:
            names_images.append(image.split("/")[-1])
    product.images = names_images
    return product.images


def check_news_img(news: SNewsDetail) -> str:
    image_directory = "app/static/images/"
    if not os.path.exists(f"{image_directory}{news.news_image_name}"):
        news.image_name = None
    
    return news.news_image_name
