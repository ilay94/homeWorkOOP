import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone
from src.сategory import Category


@pytest.fixture(scope="function")
def product_init():
    return Product("Samsung Test Ultra", "Описание", 500.0, 5)


@pytest.fixture(scope="function")
def smartphone_init():
    return Smartphone("Samsung Test Ultra", "Описание", 500.0, 5, 99.9, "Test Ultra", 100, "Серый")


@pytest.fixture(scope="function")
def product_init_alt():
    return Product("Xiaomi Test Ultra", "Описание", 250.0, 10)


@pytest.fixture(scope="function")
def smartphone_init_alt():
    return Smartphone("Xiaomi Test Ultra", "Описание", 250.0, 10, 99.9, "Test Ultra", 10, "Золотой")


@pytest.fixture(scope="function")
def lawngrass_init():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture(scope="function")
def lawngrass_init_alt():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_init(product_init):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [product_init],
    )


@pytest.fixture
def category_tv_init(product_init):
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_init],
    )


@pytest.fixture
def category_init_empy_product():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [],
    )


@pytest.fixture
def product_init_list(product_init, product_init_alt):
    return [product_init, product_init_alt]
