import pytest

from src.category import Category
from src.product import Product


# Фикстуры для тестов
@pytest.fixture
def first_category():
    """Фикстура для первой категории с товарами."""
    product1 = Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )
    product2 = Product(
        name="Samsung Galaxy S21",
        description="256GB, Черный",
        price=60000.0,
        quantity=5,
    )
    return Category(
        name="Смартфоны",
        description="Смартфоны для удобства жизни",
        products=[product1, product2],
    )


@pytest.fixture
def second_category():
    """Фикстура для второй категории с товарами."""
    product1 = Product(
        name="iPhone 13", description="128GB, Синий", price=70000.0, quantity=8
    )
    product2 = Product(
        name="Google Pixel 6", description="256GB, Белый", price=65000.0, quantity=10
    )
    return Category(
        name="Смартфоны",
        description="Смартфоны для удобства жизни",
        products=[product1, product2],
    )


@pytest.fixture
def third_category():
    """Фикстура для третьей категории без товаров."""
    return Category(name="Телевизоры", description="Современные телевизоры")


# Фикстура для сброса классовых атрибутов
@pytest.fixture(autouse=True)
def reset_class_attributes():
    """Фикстура для сброса классовых атрибутов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield


# Старые тесты
def test_category_init(first_category, second_category):
    """Тест инициализации категории с товарами."""
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны для удобства жизни"
    assert len(first_category.products.split("\n")) == 2  # Проверка количества товаров
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert (
            first_category.product_count == 4
    )  # Общее количество товаров в двух категориях
    assert second_category.product_count == 4


def test_category_init_without_products(third_category):
    """Тест инициализации категории без товаров."""
    assert third_category.name == "Телевизоры"
    assert third_category.description == "Современные телевизоры"
    assert third_category.products == ""  # Список товаров пуст
    assert third_category.product_count == 0  # product_count не должен измениться


# Новые тесты
def test_add_product(first_category):
    """Тест добавления товара в категорию."""
    new_product = Product(
        name="OnePlus 9", description="256GB, Черный", price=50000.0, quantity=7
    )
    first_category.add_product(new_product)
    assert (
            len(first_category.products.split("\n")) == 3
    )  # Количество товаров увеличилось
    assert first_category.product_count == 3  # Общее количество товаров увеличилось


def test_products_getter(first_category):
    """Тест геттера для списка товаров."""
    products = first_category.products
    assert "Xiaomi Redmi Note 11" in products
    assert "Samsung Galaxy S21" in products
    assert "31000.0 руб." in products
    assert "60000.0 руб." in products


def test_category_count(first_category, second_category, third_category):
    """Тест классового атрибута category_count."""
    assert Category.category_count == 3  # Три категории созданы


def test_product_count(first_category, second_category, third_category):
    """Тест классового атрибута product_count."""
    assert Category.product_count == 4  # Общее количество товаров в двух категориях
