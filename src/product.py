class Product:
    """Класс описывающий продукт"""

    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str = ""):
        if type(name) is not str:
            raise TypeError("Имя продукта должно быть строкой")
        self.name = name
        if type(description) is not str:
            raise TypeError("Описание продукта должно быть строкой")
        self.description = description
        if type(price) is not float:
            raise TypeError("Цена продукта должна быть числом")
        self.__price = price
        if not type(quantity) in (int, float):
            raise TypeError("Количество продукта должно быть целым")
        self.quantity = quantity
        if type(color) is not str:
            raise TypeError("Цвет продукта должен быть строкой")
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складываем товары, учитываем цены и количество"""
        if isinstance(other, Product) and type(other) is type(self):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Аргументы должны быть класса Product")

    @property
    def price(self) -> float:
        """Возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Устанавливает цену на продукт, проверяет на отрицательность, проверяет на уменьшение цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            while True:
                user_answer = input("Новая цена меньше, понизить цену товара? [y (Да)\\ n (Нет)]").lower()
                if user_answer == "n":
                    return
                elif user_answer == "y":
                    break
        self.__price = new_price

    @classmethod
    def new_product(cls, product_params: dict, product_list=None):
        """Создает новый продукт по переданному словарю, может проверять наличие похожего товара в переданном списке"""
        if product_list is None:
            product_list = []
        if len(product_list) > 0 and product_params.get("name") in [p.name for p in product_list]:
            for old_product in product_list:
                if old_product.name == product_params.get("name"):
                    old_product.quantity += product_params.get("quantity")
                    if old_product.price < product_params.get("price"):
                        old_product.price = product_params.get("price")
                    return old_product
        else:
            return Product(
                product_params.get("name"),
                product_params.get("description"),
                product_params.get("price"),
                product_params.get("quantity"),
            )
