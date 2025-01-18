import os

from src.category import Category


def test_read_json():
    """Тест функции read_json."""
    from src.utils import read_json

    json_path = os.path.join("data", "products.json")

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    full_json_path = os.path.join(project_root, json_path)

    data = read_json(full_json_path)

    assert isinstance(data, list)
    assert len(data) == 2

    # Проверка первой категории
    assert data[0]["name"] == "Смартфоны"
    assert (
            data[0]["description"]
            == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(data[0]["products"]) == 3

    assert data[0]["products"][1]["name"] == "Iphone 15"
    assert data[0]["products"][1]["price"] == 210000.0
    assert data[0]["products"][1]["quantity"] == 8

    assert data[1]["name"] == "Телевизоры"
    assert (
            data[1]["description"]
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(data[1]["products"]) == 1


def test_create_object_from_json():
    """Тест функции create_object_from_json."""
    from src.utils import create_object_from_json, read_json

    json_path = os.path.join("data", "products.json")

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    full_json_path = os.path.join(project_root, json_path)

    data = read_json(full_json_path)

    categories = create_object_from_json(data)

    assert isinstance(categories, list)
    assert len(categories) == 2

    category1 = categories[0]
    assert isinstance(category1, Category)
    assert category1.name == "Смартфоны"
    assert (
            category1.description
            == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )

    products_str = category1.products
    assert "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products_str
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in products_str

    category2 = categories[1]
    assert isinstance(category2, Category)
    assert category2.name == "Телевизоры"
    assert (
            category2.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    products_str = category2.products
    assert '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.' in products_str
