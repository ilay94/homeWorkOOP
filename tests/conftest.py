import pytest

from src.product import Product
from src.сategory import Category


@pytest.fixture(scope="function")
def product_init():
    return Product("Samsung Test Ultra", "Описание", 500.0, 5)


@pytest.fixture(scope="function")
def product_init_alt():
    return Product("Xiaomi Test Ultra", "Описание", 250.0, 10)


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
def product_init_list(product_init, product_init_alt):
    return [product_init, product_init_alt]
