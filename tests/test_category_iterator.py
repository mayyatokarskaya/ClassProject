import pytest
from src.product import Product
from src.category import Category
from src.category_iterator import CategoryIterator

# Фикстура для создания категории с товарами
@pytest.fixture
def sample_category():
    product1 = Product("Телевизор", "4K OLED", 80000.0, 15)
    product2 = Product("Смартфон", "128GB", 50000.0, 10)
    return Category("Электроника", "Техника для дома", [product1, product2])

# Фикстура для создания пустой категории
@pytest.fixture
def empty_category():
    return Category("Пустая категория", "Нет товаров", [])

# Тест: Итератор корректно перебирает товары
def test_category_iterator(sample_category):
    iterator = CategoryIterator(sample_category)
    products = list(iterator)  # Преобразуем итератор в список

    # Проверяем, что все товары были возвращены
    assert len(products) == 2
    assert isinstance(products[0], Product)  # Проверяем, что это объект Product
    assert isinstance(products[1], Product)  # Проверяем, что это объект Product
    assert products[0].name == "Телевизор"
    assert products[1].name == "Смартфон"

# Тест: Итератор завершает итерацию после окончания товаров
def test_category_iterator_stop_iteration(sample_category):
    iterator = CategoryIterator(sample_category)

    # Перебираем все товары
    for _ in range(2):
        next(iterator)

    # Проверяем, что следующее обращение вызывает StopIteration
    with pytest.raises(StopIteration):
        next(iterator)

# Тест: Итератор корректно работает с пустой категорией
def test_category_iterator_empty_category(empty_category):
    iterator = CategoryIterator(empty_category)

    # Проверяем, что итератор сразу завершает итерацию
    with pytest.raises(StopIteration):
        next(iterator)

    # Проверяем, что список товаров пуст
    assert len(list(iterator)) == 0