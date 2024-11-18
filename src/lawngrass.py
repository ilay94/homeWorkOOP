from src.product import Product


class LawnGrass(Product):
    """Трава газонная"""

    country: str
    germination_period: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
