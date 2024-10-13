from typing import Any

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

from app.news.schemas import SNewsDetail
from app.products.schemas import SProductsDetail


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
    names_images = []
    if len(news.images) == 0:
        news.images = None
    else:
        for image in news.images:
            names_images.append(image.split("/")[-1])
    news.images = names_images
    return news.images


class ImageType(FileType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=FileSystemStorage(path='app/static/images'), *args, **kwargs)


class FileType(FileType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=FileSystemStorage(path='app/files'), *args, **kwargs)
