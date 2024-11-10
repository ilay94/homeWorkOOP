import pytest

from src.сategory import Category
from tests.conftest import product_init


def test_category_init(category_init):
    assert category_init.name == "Смартфоны"
    assert (
        category_init.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_product_count(category_tv_init):
    assert Category.category_count == 2
    assert Category.product_count == 2
    Category.product_count = 0


@pytest.mark.parametrize(
    "name, description, products, expected_exception",
    [
        (None, "Описание", [product_init], TypeError),
        ([], "Описание", [product_init], TypeError),
        ("Телефон", None, [product_init], TypeError),
        ("Телефон", [], [product_init], TypeError),
        ("Телефон", "Описание", 9, TypeError),
        ("Телефон", "Описание", [1, 2], TypeError),
    ],
)
def test_product_create(name, description, products, expected_exception):
    with pytest.raises(expected_exception):
        Category(name, description, products)


def test_products_getter(category_init):
    assert category_init.products == "Samsung Test Ultra, 500.0 руб. Остаток: 5 шт"


def test_add_product_new(category_init, product_init_alt):
    category_init.add_product(product_init_alt)
    assert category_init.product_count == 2
