from wtforms.validators import DataRequired
from sqladmin import ModelView
from wtforms import TextAreaField


from app.products.models import Products, ProductsInfo
from app.admin.columns import (
    column_labels_for_products,
    column_labels_for_products_info,
    form_columns_for_products,
    form_columsn_for_products_info
)


class ProductsAdmin(ModelView, model=Products):
    column_list = [c.name for c in Products.__table__.c] + [Products.characteristics]
    name = "Товар"
    name_plural = "Товары"
    icon = "fa-solid fa-car"

    column_labels = column_labels_for_products
    form_columns = form_columns_for_products

    form_overrides = {
        'description': TextAreaField
    }

    form_args = {
        'description': {
            'label': 'Описание',
            'validators': [DataRequired()]
        }
    }
    
    form_template = "admin/model_form.html"


class ProductsInfoAdmin(ModelView, model=ProductsInfo):
    column_list = [c.name for c in ProductsInfo.__table__.c] + [ProductsInfo.product]
    name = "Характеристика товара"
    name_plural = "Характеристики товаров"
    icon = "fa-solid fa-star"

    column_labels = column_labels_for_products_info
    form_columns = form_columsn_for_products_info
