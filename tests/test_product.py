from src.product import Product


def test_product_init():
    """Тест корректности инициализации объекта через конструктор."""
    product = Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


class TestProduct:
    def test_price_getter(self):
        """Тест геттера для цены."""
        product = Product(
            name="Телевизор", description="4K OLED", price=100000.0, quantity=5
        )
        assert product.price == 100000.0

    def test_price_setter_positive(self):
        """Тест сеттера для цены с корректным значением."""
        product = Product(
            name="Телевизор", description="4K OLED", price=100000.0, quantity=5
        )
        product.price = 120000.0
        assert product.price == 120000.0

    def test_price_setter_negative(self):
        """Тест сеттера для цены с некорректным значением (отрицательная цена)."""
        product = Product(
            name="Телевизор", description="4K OLED", price=100000.0, quantity=5
        )
        product.price = -50000.0  # Некорректное значение
        assert product.price == 100000.0  # Цена не должна измениться

    def test_price_setter_zero(self):
        """Тест сеттера для цены с нулевым значением."""
        product = Product(
            name="Телевизор", description="4K OLED", price=100000.0, quantity=5
        )
        product.price = 0  # Некорректное значение
        assert product.price == 100000.0  # Цена не должна измениться

    def test_new_product_full_data(self):
        """Тест создания объекта через new_product с полным набором данных."""
        product_data = {
            "name": "Ноутбук",
            "description": "16GB RAM, 512GB SSD",
            "price": 75000.0,
            "quantity": 10,
        }
        product = Product.new_product(product_data)
        assert product.name == "Ноутбук"
        assert product.description == "16GB RAM, 512GB SSD"
        assert product.price == 75000.0
        assert product.quantity == 10

    def test_new_product_partial_data(self):
        """Тест создания объекта через new_product с частичным набором данных."""
        product_data = {"name": "Мышь", "price": 1500.0}
        product = Product.new_product(product_data)
        assert product.name == "Мышь"
        assert product.description == ""  # Значение по умолчанию
        assert product.price == 1500.0
        assert product.quantity == 0  # Значение по умолчанию

    def test_new_product_empty_data(self):
        """Тест создания объекта через new_product без данных."""
        product = Product.new_product()
        assert product.name == ""  # Значение по умолчанию
        assert product.description == ""  # Значение по умолчанию
        assert product.price == 0.0  # Значение по умолчанию
        assert product.quantity == 0  # Значение по умолчанию
