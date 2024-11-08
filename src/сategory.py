from src.product import Product


class Category:
    """Класс описывающий категорию и содержит список товаров в этой категории"""
    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        Category.category_count+=1
        self.products = products
        for product in products:
            Category.product_count+=product.quantity
