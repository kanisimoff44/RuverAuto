from typing import Any
from fastapi import Request
from wtforms.validators import DataRequired
from sqladmin import ModelView
from wtforms import TextAreaField, SelectField


from app.products.models import Products, ProductsInfo
from app.main_content.models import MainContent
from app.news.models import News
from app.users.models import Users
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
    form_column_for_news
)
from app.users.auth import get_password_hash


class ProductsAdmin(ModelView, model=Products):
    column_list = [
        Products.id,
        Products.name,
        Products.image_name,
        Products.is_active,
        Products.description
    ] + [Products.characteristics]

    name = "Товар"
    name_plural = "Товары"
    icon = "fa-solid fa-car"

    column_labels = column_labels_for_products
    form_columns = form_columns_for_products

    form_overrides = {
        "description": TextAreaField,
        "aligment": SelectField
    }

    form_args = {
        "description": {
            "label": "Описание",
            "validators": [DataRequired()]
        },
        'alignment': {
            'choices': [('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]
        }
    }


class ProductsInfoAdmin(ModelView, model=ProductsInfo):
    column_list = [c.name for c in ProductsInfo.__table__.c] + [ProductsInfo.product]
    name = "Характеристика товара"
    name_plural = "Характеристики товаров"
    icon = "fa-solid fa-star"

    column_labels = column_labels_for_products_info
    form_columns = form_columsn_for_products_info


class MainContentAdmin(ModelView, model=MainContent):
    column_list = [c.name for c in MainContent.__table__.c]
    name = "Поля контента"
    name_plural = "Контент"
    icon = "fa-solid fa-brush"
    can_delete = False

    column_labels = column_labels_for_main_content
    form_columns = form_column_for_main_content


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
