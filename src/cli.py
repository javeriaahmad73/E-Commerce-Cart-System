from models import Product, ShoppingCart, PercentageDiscount


def main():

    cart = ShoppingCart(PercentageDiscount(10))

    p1 = Product("P101", "Laptop", 1000)
    p2 = Product("P102", "Mouse", 50)

    cart.add(p1, 1)
    cart.add(p2, 2)

    print("Subtotal:", cart.subtotal())
    print("Total after discount:", cart.total())


if __name__ == "__main__":
    main()