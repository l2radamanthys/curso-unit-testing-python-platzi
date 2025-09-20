from decimal import Decimal, ROUND_HALF_UP


def calculate_total(products, discount=0):
    total = Decimal('0')
    for product in products:
        total += Decimal(str(product['price']))
    
    discount = Decimal(str(discount))

    total -= total * (discount / 100)
    
    # Redondear a 2 decimales
    return float(total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))


def test_calculate_total_with_empty_list():
    assert calculate_total([], 10) == 0


def test_calculate_total_with_single_products():
    assert calculate_total([{'name': 'apple', 'price': 1.0}], 25) == 0.75
    assert calculate_total([{'name': 'banana', 'price': 0.5}], 10) == 0.45


def test_calculate_total_with_multiple_products():
    products = [
        {'name': 'apple', 'price': 1.0},
        {'name': 'banana', 'price': 0.14},
        {'name': 'grape', 'price': 0.01},
        {'name': 'orange', 'price': 0.75}
    ]
    assert calculate_total(products, 5) == 1.81


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_products()
    test_calculate_total_with_multiple_products()
    print("All tests passed.")