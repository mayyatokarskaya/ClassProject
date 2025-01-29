from src.product import Product


class Smartphone(Product):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ):
        """Инициализация класса Smartphone"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


if __name__ == "__main__":
    product = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        "15",
        "Ifone",
        "256 ГБ",
        "grey",
    )

    print(str(product))
    print(product.description)
    print(product.efficiency)
