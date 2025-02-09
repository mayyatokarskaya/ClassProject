from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация базового продукта"""
        self.name = name
        self.description = description
        self.price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    @classmethod
    @abstractmethod
    def new_product(cls, product_data=None):
        """Создание нового продукта из словаря"""
        pass

    @abstractmethod
    def __str__(self):
        """Возвращает строковое представление продукта"""
        pass
