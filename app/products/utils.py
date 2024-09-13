import os

from app.products.schemas import SProductsDetail


def check_img(product: SProductsDetail) -> str:
    image_directory = "app/static/images/"
    if not os.path.exists(f"{image_directory}{product.image_name}"):
        product.image_name = None
    
    return product.image_name
