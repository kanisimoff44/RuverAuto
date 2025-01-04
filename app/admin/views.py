from typing import Any

from fastapi import Request
from sqladmin import ModelView
from wtforms import TextAreaField, FileField

from app.admin.columns import (
    column_labels_for_about_us_images,
    column_labels_for_main_content,
    column_labels_for_news,
    column_labels_for_news_images,
    column_labels_for_price_list,
    column_labels_for_producst_images,
    column_labels_for_products,
    column_labels_for_products_info,
    column_labels_for_text_pages,
    column_labels_for_users,
    form_column_for_main_content,
    form_column_for_news,
    form_column_for_price_list,
    form_column_for_users,
    form_columns_for_products,
    form_columns_for_producst_images
)
from app.main_content.models import AboutUsImages, MainContent
from app.news.models import News, NewsImages
from app.products.models import PriceList, Products, ProductsImages, ProductsInfo
from app.text_pages.models import TextPages
from app.users.auth import get_password_hash
from app.users.models import Users


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

    name = "товар"
    name_plural = "Товары"
    icon = "fa-solid fa-car"

    column_labels = column_labels_for_products
    form_columns = form_columns_for_products

    form_overrides = {
        "description": TextAreaField,
    }


class ProductsImagesAdmin(ModelView, model=ProductsImages):
    column_list = [c.name for c in ProductsImages.__table__.c] + [ProductsImages.product]
    name = "изображение товара"
    name_plural = "Изображения товаров"
    icon = "fa-solid fa-image"

    column_labels = column_labels_for_producst_images
    form_columns = form_columns_for_producst_images

    form_overrides = {
        "image_name": FileField,
    }


class ProductsInfoAdmin(ModelView, model=ProductsInfo):
    column_list = [c.name for c in ProductsInfo.__table__.c] + [ProductsInfo.product]
    name = "характеристику товара"
    name_plural = "Характеристики товаров"
    icon = "fa-solid fa-star"

    column_labels = column_labels_for_products_info


class PriceListAdmin(ModelView, model=PriceList):
    column_list = [c.name for c in PriceList.__table__.c]
    name = "прайс-лист"
    name_plural = "Прайс-листы"
    icon = "fa-solid fa-money-bill-1-wave"
    
    form_overrides = {
        "file_name": FileField,
    }

    column_labels = column_labels_for_price_list
    form_columns = form_column_for_price_list


class MainContentAdmin(ModelView, model=MainContent):
    column_list = [c.name for c in MainContent.__table__.c] + [MainContent.images]
    name = "новую настройку"
    name_plural = "Настройка сайта"
    icon = "fa-solid fa-brush"
    can_delete = False

    column_labels = column_labels_for_main_content
    form_columns = form_column_for_main_content
    
    form_overrides = {
        "main_desc": TextAreaField
    }


class AboutUsAdmin(ModelView, model=AboutUsImages):
    column_list = [c.name for c in AboutUsImages.__table__.c] + [AboutUsImages.about_us]
    name = "изображение «О нас»"
    name_plural = "Изображения «О нас»"
    icon = "fa-solid fa-image"

    column_labels = column_labels_for_about_us_images


class TextPagesAdmin(ModelView, model=TextPages):
    column_list = [c.name for c in TextPages.__table__.c]
    name = "текстовую страница"
    name_plural = "Текстовые страницы"
    icon = "fa-solid fa-file-lines"
    can_delete = False
    
    column_labels = column_labels_for_text_pages
    
    form_overrides = {
        "our_contacts": TextAreaField,
        "delivery_and_payment": TextAreaField,
        "privacy_policy": TextAreaField,
        "user_agreement": TextAreaField,
    }


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.username, Users.is_active, Users.is_superuser, Users.role]
    name = "пользователя"
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
        News.images,
        News.is_active,
        News.description
    ]
    name = "новость"
    name_plural = "Новости"
    icon = "fa-solid fa-newspaper"
    can_delete = True

    column_labels = column_labels_for_news
    form_columns = form_column_for_news
    
    form_overrides = {
        "description": TextAreaField
    }


class NewsImagesAdmin(ModelView, model=NewsImages):
    column_list = [c.name for c in NewsImages.__table__.c] + [NewsImages.the_news]
    name = "изображение новости"
    name_plural = "Изображения новостей"
    icon = "fa-solid fa-image"

    column_labels = column_labels_for_news_images
