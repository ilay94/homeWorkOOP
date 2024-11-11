import pytest

from src.iteratorProductInCategory import IteratorProductInCategory


def test_iterator_product_in_category(category_init):
    iterator = IteratorProductInCategory(category_init)
    assert str(next(iterator)) == "Samsung Test Ultra, 500.0 руб. Остаток: 5 шт."
    with pytest.raises(StopIteration):
        next(iterator)
    iter(iterator)
    assert str(next(iterator)) == "Samsung Test Ultra, 500.0 руб. Остаток: 5 шт."
