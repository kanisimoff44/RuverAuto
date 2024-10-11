from typing import Any
from fastapi import Request
from sqladmin import ModelView
from starlette.datastructures import UploadFile
from wtforms import TextAreaField, MultipleFileField
import aiofiles

from app.products.models import Products, ProductsInfo, PriceList, ProductsImages
from app.main_content.models import MainContent
from app.news.models import News
from app.users.models import Users
from app.text_pages.models import TextPages
from app.admin.columns import (
    column_labels_for_products,
    column_labels_for_products_info,
    form_columns_for_products,
    form_columsn_for_products_info,
    column_labels_for_main_content,
    form_column_for_main_content,
    column_labels_for_users,
    form_column_for_users,
    column_labels_for_news,
    form_column_for_news,
    column_labels_for_price_list,
    form_column_for_price_list,
    column_labels_for_text_pages,
    form_column_for_text_pages,
    column_labels_for_producst_images,
    form_column_for_producst_images
)
from app.users.auth import get_password_hash
from werkzeug.utils import secure_filename


class ProductsAdmin(ModelView, model=Products):
    column_list = [
        Products.id,
        Products.name,
        Products.images,
        Products.price,
        Products.label,
        Products.is_active,
        Products.characteristics,
        Products.description
    ]

    name = "Товар"
    name_plural = "Товары"
    icon = "fa-solid fa-car"

    column_labels = column_labels_for_products
    form_columns = form_columns_for_products

    form_overrides = {
        "description": TextAreaField,
    }
    

class ProductsImagesAdmin(ModelView, model=ProductsImages):
    column_list = [c.name for c in ProductsImages.__table__.c] + [ProductsImages.product]
    name = "Изображения товаров"
    name_plural = "Изображение товара"
    icon = "fa-solid fa-image"

    column_labels = column_labels_for_producst_images
    form_columns = form_column_for_producst_images


class ProductsInfoAdmin(ModelView, model=ProductsInfo):
    column_list = [c.name for c in ProductsInfo.__table__.c] + [ProductsInfo.product]
    name = "Характеристика товара"
    name_plural = "Характеристики товаров"
    icon = "fa-solid fa-star"

    column_labels = column_labels_for_products_info
    form_columns = form_columsn_for_products_info


class PriceListAdmin(ModelView, model=PriceList):
    column_list = [c.name for c in PriceList.__table__.c]
    name = "Прайс-лист"
    name_plural = "Прайс-листы"
    icon = "fa-solid fa-money-bill-1-wave"

    column_labels = column_labels_for_price_list
    form_columns = form_column_for_price_list


class MainContentAdmin(ModelView, model=MainContent):
    column_list = [c.name for c in MainContent.__table__.c]
    name = "Поле сайта"
    name_plural = "Настройка сайта"
    icon = "fa-solid fa-brush"
    can_delete = False

    column_labels = column_labels_for_main_content
    form_columns = form_column_for_main_content


class TextPagesAdmin(ModelView, model=TextPages):
    column_list = [c.name for c in TextPages.__table__.c]
    name = "Текстовая страница"
    name_plural = "Текстовые страницы"
    icon = "fa-solid fa-file-lines"
    can_delete = False
    
    column_labels = column_labels_for_text_pages
    form_columns = form_column_for_text_pages
    
    form_overrides = {
        "our_contacts": TextAreaField,
        "delivery_and_payment": TextAreaField,
        "privacy_policy": TextAreaField,
        "user_agreement": TextAreaField,
    }


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.email, Users.is_active, Users.is_superuser, Users.role]
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    can_delete = False

    column_labels = column_labels_for_users
    form_columns = form_column_for_users

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request) -> None:
        data["hashed_password"] = get_password_hash(data["hashed_password"])
        return await super().on_model_change(data, model, is_created, request)


class NewsAdmin(ModelView, model=News):
    column_list = [
        News.id,
        News.title,
        News.date_of_the_news,
        News.news_image_name,
        News.is_active,
        News.description
    ]
    name = "Новость"
    name_plural = "Новости"
    icon = "fa-solid fa-newspaper"
    can_delete = True

    column_labels = column_labels_for_news
    form_columns = form_column_for_news
    
    form_overrides = {
        "description": TextAreaField
    }
