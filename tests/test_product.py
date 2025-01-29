import pytest

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
        with pytest.raises(
                ValueError, match="Цена не должна быть нулевая или отрицательная"
        ):
            product.price = -5000  # Попытка установить цену 0 должна вызвать исключение
        assert product.price == 100000.0  # Цена не должна измениться

    def test_price_setter_zero(self):
        """Тест сеттера для цены с нулевым значением."""
        product = Product(
            name="Телевизор", description="4K OLED", price=100000.0, quantity=5
        )
        with pytest.raises(
                ValueError, match="Цена не должна быть нулевая или отрицательная"
        ):
            product.price = 0  # Попытка установить цену 0 должна вызвать исключение
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
        assert product.price == 1.0  # Значение по умолчанию
        assert product.quantity == 0  # Значение по умолчанию

    def test_product_str(self):
        """Тест магического метода __str__."""
        product = Product(
            name="Телевизор", description="4K OLED", price=100000.0, quantity=5
        )
        expected_output = "Телевизор, 100000.0 руб. Остаток: 5 шт."
        assert str(product) == expected_output

    def test_product_add_valid(self):
        """Тест магического метода __add__ с корректными объектами."""
        product1 = Product(
            name="Телевизор", description="4K OLED", price=100000.0, quantity=2
        )
        product2 = Product(
            name="Смартфон", description="128GB", price=50000.0, quantity=3
        )
        total_value = product1 + product2
        assert total_value == (100000.0 * 2) + (50000.0 * 3)

    def test_product_add_invalid(self):
        """Тест магического метода __add__ с некорректным объектом."""
        product = Product(
            name="Телевизор", description="4K OLED", price=100000.0, quantity=2
        )
        invalid_object = "Не продукт"

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            product + invalid_object
