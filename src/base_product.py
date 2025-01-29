from abc import ABC, abstractmethod

class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация базового продукта"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    @abstractmethod
    def new_product(cls, product_data=None):
        """Создание нового продукта из словаря"""
        pass

    @abstractmethod
    def __str__(self):
        """Возвращает строковое представление продукта"""
        pass


