from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс описывающий продукт"""

    name: str
    description: str
    __price: float
    quantity: int
    color: str

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_params: dict, product_list=None):
        pass
