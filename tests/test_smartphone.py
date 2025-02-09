from src.smartphone import Smartphone


def test_smartphone_init(smartphone_valid):
    """Тест инициализации объекта Smartphone."""
    smartphone = smartphone_valid
    assert smartphone.name == "iPhone 13"
    assert smartphone.model == "A2634"
    assert smartphone.memory == 128
    assert smartphone.efficiency == 3.2
    assert smartphone.color == "Синий"


def test_smartphone_empty_data():
    """Тест создания смартфона с пустыми данными."""
    smartphone = Smartphone(
        name="",
        description="",
        price=1.0,
        quantity=1,
        efficiency=0.0,
        model="",
        memory=0,
        color="",
    )
    assert smartphone.name == ""
    assert smartphone.price == 1.0
    assert smartphone.quantity == 1


def test_smartphone_boundary_values():
    """Тест с граничными значениями."""
    smartphone = Smartphone(
        name="Xiaomi Mi 10",
        description="64GB, Черный",
        price=1.0,  # Минимальная допустимая цена
        quantity=1,  # Минимальное количество
        efficiency=0.1,  # Минимальная производительность
        model="MI10",
        memory=64,  # Минимальная память
        color="Черный",
    )
    assert smartphone.price == 1.0
    assert smartphone.quantity == 1
    assert smartphone.efficiency == 0.1
    assert smartphone.memory == 64


def test_smartphone_price_setter(smartphone_valid):
    """Тест установки новой цены через сеттер."""
    smartphone = smartphone_valid
    smartphone.price = 75000.0
    assert smartphone.price == 75000.0


def test_smartphone_update_attributes(smartphone_valid):
    """Тест обновления атрибутов объекта Smartphone."""
    smartphone = smartphone_valid

    smartphone.name = "iPhone 14"
    smartphone.color = "Красный"
    smartphone.memory = 256

    assert smartphone.name == "iPhone 14"
    assert smartphone.color == "Красный"
    assert smartphone.memory == 256
