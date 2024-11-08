import pytest

from src.product import Product


def test_product_init(product_init):
    assert product_init.name == "Samsung Test Ultra"
    assert product_init.description == "Описание"
    assert product_init.price == 500.0
    assert product_init.quantity == 5


@pytest.mark.parametrize(
    "name, description, price, quantity, expected_exception",
    [
        (None, "Описание", 500.0, 1, TypeError),
        ([], "Описание", 500.0, 1, TypeError),
        ("Samsung Test Ultra", None, 500.0, 1, TypeError),
        ("Samsung Test Ultra", [], 500.0, 1, TypeError),
        ("Samsung Test Ultra", "Описание", [], 1, TypeError),
        ("Samsung Test Ultra", "Описание", None, 1, TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, [], TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, None, TypeError),
    ],
)
def test_product_create(name, description, price, quantity, expected_exception):
    with pytest.raises(expected_exception):
        Product(name, description, price, quantity)
