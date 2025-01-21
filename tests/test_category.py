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


def test_category_str(first_category):
    """Тест магического метода __str__."""
    expected_output = "Смартфоны, количество штук: 19 шт."
    assert str(first_category) == expected_output


def test_get_products_list(first_category):
    """Тест метода get_products_list."""
    products = first_category.get_products_list()
    assert isinstance(products, list)  # Проверяем, что возвращается список
    assert len(products) == 2  # Проверяем количество товаров
    assert all(
        isinstance(product, Product) for product in products
    )  # Все элементы — объекты Product


def test_category_iteration(first_category):
    """Тест итерации по категории."""
    products = list(first_category)  # Преобразуем итератор в список
    assert len(products) == 2  # Проверяем количество товаров
    assert all(
        isinstance(product, Product) for product in products
    )  # Все элементы — объекты Product
    assert products[0].name == "Xiaomi Redmi Note 11"
    assert products[1].name == "Samsung Galaxy S21"


def test_add_invalid_product(first_category):
    """Тест добавления некорректного товара."""
    invalid_product = "Не продукт"
    first_category.add_product(invalid_product)
    assert (
            len(first_category.get_products_list()) == 2
    )  # Количество товаров не изменилось
    assert first_category.product_count == 2  # Общее количество товаров не изменилось


def test_class_attributes():
    """Тест классовых атрибутов category_count и product_count."""
    # Создаем две категории с товарами
    product1 = Product("Телевизор", "4K OLED", 100000.0, 5)
    product2 = Product("Смартфон", "128GB", 50000.0, 10)
    category1 = Category("Электроника", "Техника для дома", [product1])
    category2 = Category("Смартфоны", "Смартфоны для удобства жизни", [product2])

    # Проверяем классовые атрибуты
    assert Category.category_count == 2
    assert Category.product_count == 2

    # Проверяем атрибуты второй категории
    assert category2.name == "Смартфоны"
    assert category2.description == "Смартфоны для удобства жизни"

    # Добавляем товар в одну из категорий
    product3 = Product("Ноутбук", "16GB RAM", 75000.0, 3)
    category1.add_product(product3)

    # Проверяем обновленные классовые атрибуты
    assert Category.product_count == 3
