import pytest

from src.smartphone import Smartphone


def test_smartphone_init(smartphone_init):
    assert smartphone_init.name == "Samsung Test Ultra"
    assert smartphone_init.description == "Описание"
    assert smartphone_init.price == 500.0
    assert smartphone_init.quantity == 5
    assert smartphone_init.efficiency == 99.9
    assert smartphone_init.model == "Test Ultra"
    assert smartphone_init.memory == 100
    assert smartphone_init.color == "Серый"


def test_smartphone_add(smartphone_init, smartphone_init_alt, product_init):
    assert smartphone_init + smartphone_init_alt == 5000.0
    with pytest.raises(TypeError):
        result = product_init + smartphone_init
        print(result)


@pytest.mark.parametrize(
    "name, description, price, quantity, efficiency, model, memory, color, expected_exception",
    [
        (None, "Описание", 500.0, 1, 99.9, "Test Ultra", 100, "Серый", TypeError),
        ([], "Описание", 500.0, 1, 99.9, "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", None, 500.0, 1, 99.9, "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", [], 500.0, 1, 99.9, "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", [], 1, 99.9, "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", None, 1, 99.9, "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, [], 99.9, "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, None, 99.9, "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, "99.9", "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, [], "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, None, "Test Ultra", 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, 99.9, [], 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, 99.9, 1, 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, 99.9, None, 100, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, 99.9, "Test Ultra", [], "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, 99.9, "Test Ultra", None, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, 99.9, "Test Ultra", 1.1, "Серый", TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, 99.9, "Test Ultra", 100, [], TypeError),
        ("Samsung Test Ultra", "Описание", 500.0, 1, 99.9, "Test Ultra", 100, None, TypeError),
    ],
)
def test_smartphone_incorrect_init(
    name, description, price, quantity, efficiency, model, memory, color, expected_exception
):
    with pytest.raises(expected_exception):
        Smartphone(name, description, price, quantity, efficiency, model, memory, color)
