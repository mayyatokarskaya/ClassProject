class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализируем класс Product"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data=None):
        """Класс-метод для создания нового объекта Product из словаря"""
        if product_data is None:
            product_data = {}  # Используем пустой словарь по умолчанию

            # Извлекаем значения из словаря с использованием значений по умолчанию
        name = product_data.get("name", "")
        description = product_data.get("description", "")
        price = product_data.get("price", 0.0)
        quantity = product_data.get("quantity", 0)

        # Создаем и возвращаем новый экземпляр класса Product
        return cls(name, description, price, quantity)



