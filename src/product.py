class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализируем класс Product"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод для сложения двух объектов класса"""
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        """Геттер для получения значения цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для установки значения цены с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data=None):
        """Класс-метод для создания нового объекта Product из словаря"""
        if product_data is None:
            product_data = {}

        name = product_data.get("name", "")
        description = product_data.get("description", "")
        price = product_data.get("price", 0.0)
        quantity = product_data.get("quantity", 0)

        return cls(name, description, price, quantity)
