from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_repr(capsys):
    """Тестирует, что PrintMixin вызывает __repr__ в Product"""
    product = Product("TestName", "TestDescription", 100.0, 10)  # noqa: F841
    captured = capsys.readouterr()  # Захватываем вывод __repr__ из __init__
    expected_repr = "Product(TestName, TestDescription, 100.0, 10)\n"
    assert captured.out == expected_repr


def test_smartphone_repr(capsys):
    """Тестирует, что PrintMixin вызывает __repr__ в Smartphone"""
    smartphone = Smartphone(  # noqa: F841
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        "15",
        "Ifone",
        256,
        "grey",
    )
    captured = capsys.readouterr()  # Захватываем вывод __repr__ из __init__
    expected_repr = "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n"
    assert captured.out == expected_repr


def test_lawn_grass_repr(capsys):
    """Тестирует, что PrintMixin вызывает __repr__ в LawnGrass"""
    lawn_grass = LawnGrass(  # noqa: F841
        "Газонная трава Лилипут",
        "Медленный рост, высокая устойчивость",
        1200.0,
        50,
        "Россия",
        "14 дней",
        "Зеленый",
    )
    captured = capsys.readouterr()  # Захватываем вывод __repr__ из __init__
    expected_repr = "LawnGrass(Газонная трава Лилипут, Медленный рост, высокая устойчивость, 1200.0, 50)\n"
    assert captured.out == expected_repr
