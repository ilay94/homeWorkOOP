from src.product import Product


class Smartphone(Product):
    """Смартфоны"""

    efficiency: float
    model: str
    memory: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity, color)
        if type(efficiency) is not float:
            raise TypeError("Производительность смартфона должна быть строкой")
        self.efficiency = efficiency
        if type(model) is not str:
            raise TypeError("Модель смартфона должна быть строкой")
        self.model = model
        if type(memory) is not int:
            raise TypeError("Память смартфона должна быть целым числом")
        self.memory = memory
