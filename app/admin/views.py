from sqladmin import ModelView

from app.products.models import Products


class ProductsAdmin(ModelView, model = Products):
    column_list = [c.name for c in Products.__table__.c]
    name = "Авто"
    name_plural = "Автомобили"
    icon = "fa-solid fa-car"
    