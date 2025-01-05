class Product:
    name:str
    description:str
    price:float
    quantity:int

    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product = Product("car", "red car", 1234.5, 2)

    print(product.name)
