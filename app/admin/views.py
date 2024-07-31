from sqladmin import ModelView

from app.products.models import Products


class ProductsAdmin(ModelView, model = Products):
    column_list = [c.name for c in Products.__table__.c]
    name = "Товар"
    name_plural = "Товары"
    icon = "fa-solid fa-car"

    column_labels = {
        "id": "Идентификатор",
        "name": "Название",
        "description": "Описание",
        "brand": "Марка",
        "condition": "Состояние",
        "year": "Год выпуска",
        "model": "Модель",
        "target": "Назначение",
        "lifting_capacity": "Грузоподьемность, кг.",
        "body_volume": "Объеи кузова, куб. м.",
        "number_of_axes": "Количество осей",
        "suspension_type": "Тип подвески",
        "weight_without_load": "Масса без нагрузки, кг.",
        "axle_brand": "Марка осей",
        "type_of_brakes": "Тип тормозов",
        "ssu_height": "Высота ССУ, мм.",
        "internal_dimensions": "Внутренние габариты, мм.",
        "phone": "Телефон",
        "specifications_id": "Спецификация",
        "country": "Страна",
        "type_of_TS": "Тип ТС",
        "engine_volume": "Объем двигателя",
        "type_of_fuel": "Тип топлива",
        "image_id": "Фото",
    }

    form_columns = {
        "name": {
            "label": "Название",
            "description": "Введите название товара"
        },
        "description": {
            "label": "Описание",
            "description": "Введите описание товара"
        },
        "brand": {
            "label": "Марка",
            "description": "Введите марку"
        },
        "condition": {
            "label": "Состояние",
            "description": "Введите состояние"
        },
        "year": {
            "label": "Год выпуска",
            "description": "Введите год выпуска"
        },
        "model": {
            "label": "Модель",
            "description": "Введите модель"
        },
        "target": {
            "label": "Назначение",
            "description": "Введите назначение товара"
        },
        "lifting_capacity": {
            "label": "Описание",
            "description": "Введите грузоподьемность, кг."
        },
        "body_volume": {
            "label": "Объеи кузова, куб. м.",
            "description": "Введите объеи кузова, куб. м."
        },
        "number_of_axes": {
            "label": "Количество осей",
            "description": "Введите количество осей"
        },
        "suspension_type": {
            "label": "Тип подвески",
            "description": "Введите тип подвески"
        },
        "weight_without_load": {
            "label": "Масса без нагрузки, кг.",
            "description": "Введите массу без нагрузки, кг."
        },
        "axle_brand": {
            "label": "Марка осей",
            "description": "Введите марку осей"
        },
        "type_of_brakes": {
            "label": "Тип тормозов",
            "description": "Введите тип тормозов"
        },
        "ssu_height": {
            "label": "Высота ССУ, мм.",
            "description": "Введите высоту ССУ, мм."
        },
        "internal_dimensions": {
            "label": "Внутренние габариты, мм.",
            "description": "Введите внутренние габариты, мм."
        },
        "phone": {
            "label": "Телефон",
            "description": "Введите телефон"
        },
        "specifications_id": {
            "label": "Спецификация",
            "description": "Введите идентификатор спецификации"
        },
        "country": {
            "label": "Страна",
            "description": "Введите страну"
        },
        "type_of_TS": {
            "label": "Тип ТС",
            "description": "Введите тип ТС"
        },
        "engine_volume": {
            "label": "Объем двигателя",
            "description": "Введите объем двигателя"
        },
        "type_of_fuel": {
            "label": "Тип топлива",
            "description": "Введите тип топлива"
        },
        "image_id": {
            "label": "Фото",
            "description": "Введите идентификатор фото товара"
        },
    }
