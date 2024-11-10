from src.product import Product


class Category:
    """Класс описывающий категорию и содержит список товаров в этой категории"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        if type(name) is not str:
            raise TypeError("Имя категории должно быть строкой")
        self.name = name
        if type(description) is not str:
            raise TypeError("Описание категории должно быть строкой")
        self.description = description
        if type(products) is not list:
            raise TypeError("Продукты должны быть переданы списком")
        for product in products:
            if type(product) is not Product:
                raise TypeError("В списке переданы не продуты")
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
