from unittest.mock import patch

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


@pytest.mark.parametrize(
    "new_price, expected_price, user_inputs, expected_output",
    [
        (600.0, 600.0, [""], ""),
        (0.0, 500.0, [""], "Цена не должна быть нулевая или отрицательная"),
        (-10.0, 500.0, [""], "Цена не должна быть нулевая или отрицательная"),
        (300.0, 300.0, ["y"], ""),
        (300.0, 500.0, ["n"], ""),
    ],
)
def test_price(capsys, product_init, new_price, expected_price, user_inputs, expected_output):
    with patch("builtins.input", side_effect=user_inputs):
        product_init.price = new_price

    captured = capsys.readouterr()
    assert expected_output in captured.out
    assert product_init.price == expected_price


@pytest.mark.parametrize(
    "product_params, product_list, expected_price, expected_quantity",
    [
        ({"name": "Samsung Test Ultra", "description": "Описание", "price": 500.0, "quantity": 5}, None, 500.0, 5),
        (
            {"name": "Samsung Test Ultra", "description": "Описание", "price": 500.0, "quantity": 5},
            [],
            500.0,
            5,
        ),
    ],
)
def test_new_product_empty_list(product_params, product_list, expected_price, expected_quantity):
    new_product = Product.new_product(product_params, product_list)
    assert new_product.price == expected_price
    assert new_product.quantity == expected_quantity


@pytest.mark.parametrize(
    "product_params, expected_price, expected_quantity",
    [
        (
            {"name": "Samsung Test Ultra", "description": "Описание", "price": 500.0, "quantity": 10},
            500.0,
            15,
        ),
        (
            {"name": "Samsung Test Ultra", "description": "Описание", "price": 300.0, "quantity": 10},
            500.0,
            15,
        ),
        (
            {"name": "Samsung Test Ultra", "description": "Описание", "price": 600.0, "quantity": 10},
            600.0,
            15,
        ),
    ],
)
def test_new_product_init_list(product_params, product_init_list, expected_price, expected_quantity):
    new_product = Product.new_product(product_params, product_init_list)
    assert new_product.price == expected_price
    assert new_product.quantity == expected_quantity


def test_str(product_init):
    assert str(product_init) == "Samsung Test Ultra, 500.0 руб. Остаток: 5 шт."


def test_add(product_init, product_init_alt):
    assert product_init + product_init_alt == 5000.0


@pytest.mark.parametrize("other", [("50"), ([]), (None)])
def test_add_incorrect_other(product_init, other):
    with pytest.raises(TypeError):
        result = product_init + other
        print(result)
