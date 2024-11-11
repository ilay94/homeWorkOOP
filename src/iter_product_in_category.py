from src.сategory import Category


class IterProductInCategory:
    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.get_products):
            product  = self.category.get_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

