import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_init(lawngrass_init):
    assert lawngrass_init.name == "Газонная трава"
    assert lawngrass_init.description == "Элитная трава для газона"
    assert lawngrass_init.price == 500.0
    assert lawngrass_init.quantity == 20
    assert lawngrass_init.country == "Россия"
    assert lawngrass_init.germination_period == "7 дней"
    assert lawngrass_init.color == "Зеленый"


def test_lawngrass_add(lawngrass_init, lawngrass_init_alt, product_init):
    assert lawngrass_init + lawngrass_init_alt == 16750.0
    with pytest.raises(TypeError):
        result = product_init + lawngrass_init
        print(result)


@pytest.mark.parametrize(
    "name, description, price, quantity, country, germination_period, color, expected_exception",
    [
        (None, "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый", TypeError),
        ([], "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый", TypeError),
        ("Газонная трава", None, 500.0, 20, "Россия", "7 дней", "Зеленый", TypeError),
        ("Газонная трава", [], 500.0, 20, "Россия", "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", [], 20, "Россия", "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", None, 20, "Россия", "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, "20", "Россия", "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, [], "Россия", "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, None, "Россия", "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, 12, "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, [], "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, None, "7 дней", "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", 7, "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", [], "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", None, "Зеленый", TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", 12, TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", [], TypeError),
        ("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", None, TypeError),
    ],
)
def test_smartphone_incorrect_init(
    name, description, price, quantity, country, germination_period, color, expected_exception
):
    with pytest.raises(expected_exception):
        LawnGrass(name, description, price, quantity, country, germination_period, color)
