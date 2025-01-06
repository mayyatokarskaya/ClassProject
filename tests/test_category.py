def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5

def test_category_init_without_products(third_category):
    """Проверка инициализации категории без передачи списка продуктов."""
    assert third_category.name == "Телевизоры"
    assert third_category.description == "Современные телевизоры"
    assert len(third_category.products) == 0  # products должен быть пустым списком
    assert third_category.product_count == 5  # product_count не должен измениться


