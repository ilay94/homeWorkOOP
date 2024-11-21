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
            if not isinstance(product, Product):
                raise TypeError("В списке переданы не продуты")
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum([p.quantity for p in self.__products])} шт."

    def add_product(self, product: Product):
        """Добавляет продукт в список продуктов этой категории"""
        if isinstance(product, Product) or issubclass(product.__class__, Product):
            self.__products.append(product)
        else:
            raise TypeError("Попытка добавить не продукт")
        Category.product_count += 1

    @property
    def get_products(self) -> list[Product]:
        return self.__products

    @property
    def products(self) -> str:
        """Возвращает список продуктов категории в виде текста"""
        return "\n".join([str(p) for p in self.__products])
