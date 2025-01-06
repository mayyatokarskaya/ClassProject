import pytest

from src.product import Product
from src.category import Category

@pytest.fixture
def first_category():
    return Category(
        name = "Смартфоны",
        description = "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products = [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        ]

    )

@pytest.fixture
def second_category():
    return Category(
        name = "Смартфоны",
        description = "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products = [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]

    )

@pytest.fixture
def third_category():
    return Category(
        name = "Телевизоры",
        description = "Современные телевизоры",
        products = [])


@pytest.fixture
def product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)