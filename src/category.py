from src.category_iterator import CategoryIterator
from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """инициализируем класс Category"""

        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество штук: {total_quantity} шт."

    def add_product(self, product):
        """Метод добавления товаров в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

    def __iter__(self):
        """Магический метод для поддержки итерации"""
        return CategoryIterator(self)

    @property
    def products(self):
        """Геттер для просмотра списка товаров"""
        return "\n".join([str(product) for product in self.__products])

    def get_products_list(self):
        """Метод для получения списка товаров (объектов Product)"""
        return self.__products
