import json
import os
from itertools import product

from src.product import Product
from src.category import Category


def read_json(path: str)-> dict:
    """считываем данные из json файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding='UTF -8') as file:
        data = json.load(file)
    return data

def create_object_from_json(data):
    """создаем объект из json файла"""
    ranks = []
    for rank in data:
        products = []
        for product in rank["products"]:
            products.append(Product(**product))
        rank["products"] = products
        ranks.append(Category(**rank))

    return ranks




if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    product_data = create_object_from_json(raw_data)
    print(raw_data)
    print(product_data[1].name)
    print(product_data[1].product_count)
    print(product_data[0].products)
