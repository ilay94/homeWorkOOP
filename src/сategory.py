from src.product import BaseProduct


class Category:
    """Класс описывающий категорию и содержит список товаров в этой категории"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list[BaseProduct]

    def __init__(self, name: str, description: str, products: list[BaseProduct]):
        if type(name) is not str:
            raise TypeError("Имя категории должно быть строкой")
        self.name = name
        if type(description) is not str:
            raise TypeError("Описание категории должно быть строкой")
        self.description = description
        if type(products) is not list:
            raise TypeError("Продукты должны быть переданы списком")
        for product in products:
            if not isinstance(product, BaseProduct):
                raise TypeError("В списке переданы не продуты")
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum([p.quantity for p in self.__products])} шт."

    def add_product(self, product: BaseProduct):
        """Добавляет продукт в список продуктов этой категории"""
        if isinstance(product, BaseProduct) or issubclass(product.__class__, BaseProduct):
            self.__products.append(product)
        else:
            raise TypeError("Попытка добавить не продукт")
        Category.product_count += 1

    @property
    def get_products(self) -> list[BaseProduct]:
        return self.__products

    @property
    def products(self) -> str:
        """Возвращает список продуктов категории в виде текста"""
        return "\n".join([str(p) for p in self.__products])

    def middle_price(self):
        """Возвращает среднию цену продуктов в категории"""
        try:
            if len(self.__products) == 0:
                raise ValueError("В категории отсутствуют продукты")
            return sum([p.price for p in self.__products]) / len(self.__products)
        except Exception:
            return  0.0
