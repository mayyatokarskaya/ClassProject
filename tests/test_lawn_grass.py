import pytest


def test_lawngrass_init(lawn_grass):
    """Тест инициализации объекта LawnGrass."""
    assert lawn_grass.name == "Premium Grass"
    assert lawn_grass.description == "Смесь трав для газона"
    assert lawn_grass.price == 1500.0
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == "Нидерланды"
    assert lawn_grass.germination_period == "7-10 дней"
    assert lawn_grass.color == "Зеленый"


def test_lawngrass_str(lawn_grass):
    """Тест строкового представления LawnGrass."""
    expected_output = "Premium Grass, 1500.0 руб. Остаток: 10 шт."
    assert str(lawn_grass) == expected_output


def test_lawngrass_update_quantity(lawn_grass):
    """Тест изменения количества травы."""
    lawn_grass.quantity = 20
    assert lawn_grass.quantity == 20


def test_lawngrass_price_update(lawn_grass):
    """Тест обновления цены."""
    lawn_grass.price = 1800.0
    assert lawn_grass.price == 1800.0

    with pytest.raises(
        ValueError, match="Цена не должна быть нулевая или отрицательная"
    ):
        lawn_grass.price = -500.0
