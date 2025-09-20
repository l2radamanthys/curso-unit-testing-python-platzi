import unittest
from src.calculator import sum, substrat, product, divide
import math


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), -2)

    def test_substrat(self):
        self.assertEqual(substrat(5, 3), 2)
        self.assertEqual(substrat(3, 5), -2)
        self.assertEqual(substrat(-1, -1), 0)

    def test_product_positive(self):
        self.assertEqual(product(3, 4), 12)
        self.assertEqual(product(3.5, 4), 14)

    def test_product_with_zero(self):
        self.assertEqual(product(3, 0), 0)
        self.assertEqual(product(0, 4), 0)
        self.assertEqual(product(3.4, 0), 0)

    def test_product_with_negative_numbers(self):
        self.assertEqual(product(3, -11), -33)
        self.assertEqual(product(-5, 4), -20)
        self.assertEqual(product(-17, -9), 153)

    def test_divition(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(40, 4), 10)

    def test_divition_by_zero(self):
        self.assertTrue(math.isnan(divide(19, 0)))
        self.assertTrue(math.isnan(divide(0.5, 0)))
