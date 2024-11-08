class Product:
    """Класс описывающий продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if type(name) is not str:
            raise TypeError("Имя продукта должно быть строкой")
        self.name = name
        if type(description) is not str:
            raise TypeError("Описание продукта должно быть строкой")
        self.description = description
        if type(price) is not float:
            raise TypeError("Цена продукта должна быть числом")
        self.price = price
        if not type(quantity) in (int, float):
            raise TypeError("Количество продукта должно быть целым")
        self.quantity = quantity
