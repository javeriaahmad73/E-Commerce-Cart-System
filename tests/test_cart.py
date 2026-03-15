import unittest
from src.models import Product, ShoppingCart, NoDiscount, PercentageDiscount


class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart(NoDiscount())
        self.product = Product("P1", "Phone", 500)

    def test_add_product(self):
        self.cart.add(self.product, 2)
        self.assertEqual(self.cart.subtotal(), 1000)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add(self.product, 0)

    def test_remove_product(self):
        self.cart.add(self.product, 1)
        self.cart.remove("P1")
        self.assertEqual(self.cart.subtotal(), 0)

    def test_remove_missing_product(self):
        with self.assertRaises(KeyError):
            self.cart.remove("X")

    def test_subtotal(self):
        self.cart.add(self.product, 3)
        self.assertEqual(self.cart.subtotal(), 1500)

    def test_total_with_discount(self):
        cart = ShoppingCart(PercentageDiscount(10))
        cart.add(self.product, 2)
        self.assertEqual(cart.total(), 900)

    def test_product_price_validation(self):
        with self.assertRaises(ValueError):
            Product("P2", "Bad", -10)

    def test_discount_validation(self):
        with self.assertRaises(ValueError):
            PercentageDiscount(150)


if __name__ == "__main__":
    unittest.main()