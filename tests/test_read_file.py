import os

import pytest

from src.read_file import read_json_products


def test_read_json_products_correct():
    result = read_json_products(os.path.join(os.path.dirname(__file__), "../data/products.json"))
    assert result[0].name == "Смартфоны"


@pytest.mark.parametrize(
    "file_patch, result",
    [
        ("tests/data/products_not_list.json", []),
        ("adasdad", []),
        ([], []),
        (None, []),
    ],
)
def test_read_json_from_file_incorrect_file(file_patch, result):
    assert read_json_products(file_patch) == result
