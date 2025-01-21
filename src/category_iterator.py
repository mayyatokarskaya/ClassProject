class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.get_products_list()):
            product = self.category.get_products_list()[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration