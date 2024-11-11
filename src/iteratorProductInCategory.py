from src.сategory import Category


class IteratorProductInCategory:
    """Класс создания итератора по продуктам в категории"""

    def __init__(self, category: Category):
        self.__category = category
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__category.get_products):
            product = self.__category.get_products[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration
