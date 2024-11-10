from src.product import Product


class Category:
    """Класс описывающий категорию и содержит список товаров в этой категории"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list[Product]

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
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.category_count += 1

    @property
    def products(self) -> str:
        return "\n".join([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт" for p in self.__products])
