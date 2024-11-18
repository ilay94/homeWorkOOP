from src.product import Product


class LawnGrass(Product):
    """Трава газонная"""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity, color)
        if type(country) is not str:
            raise TypeError("Строна производитель травы газонной должна быть строкой")
        self.country = country
        if type(germination_period) is not str:
            raise TypeError("Период проростания травы газонной должен быть строкой")
        self.germination_period = germination_period
