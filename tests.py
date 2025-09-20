def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0


def test_calculate_total_with_single_products():
    assert calculate_total([{'name': 'apple', 'price': 1.0}]) == 1.0
    assert calculate_total([{'name': 'banana', 'price': 0.5}]) == 0.5


def test_calculate_total_with_multiple_products():
    products = [
        {'name': 'apple', 'price': 1.0},
        {'name': 'banana', 'price': 0.1},
        {'name': 'grape', 'price': 0.01},
        {'name': 'orange', 'price': 0.75}
    ]
    assert calculate_total(products) == 2.17


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_products()
    print("All tests passed.")