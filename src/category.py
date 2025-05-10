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

    def add_product(self, product):
        """Метод добавления товаров в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Ошибка: можно добавлять только объекты класса Product.")

    @property
    def products(self):
        """Геттер для просмотра списка товаров"""
        return "\n".join(
            [
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                for product in self.__products
            ]
        )
