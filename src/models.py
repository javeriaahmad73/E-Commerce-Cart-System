from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


class PricingStrategy(ABC):

    @abstractmethod
    def calculate(self, subtotal: float) -> float:
        """Calculate final price based on pricing strategy."""
        pass


class NoDiscount(PricingStrategy):

    def calculate(self, subtotal: float) -> float:
        return subtotal


class PercentageDiscount(PricingStrategy):

    def __init__(self, percent: float):

        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")

        self.percent = percent

    def calculate(self, subtotal: float) -> float:

        discount = subtotal * (self.percent / 100)
        return subtotal - discount


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: float

    def __post_init__(self):

        if self.price < 0:
            raise ValueError("Product price cannot be negative")


@dataclass
class CartItem:
    product: Product
    qty: int = 1

    def subtotal(self) -> float:

        if self.qty < 1:
            raise ValueError("Quantity must be at least 1")

        return self.product.price * self.qty


class ShoppingCart:

    def __init__(self, strategy: PricingStrategy):

        self._items: Dict[str, CartItem] = {}
        self.strategy = strategy

    def add(self, product: Product, qty: int = 1) -> None:

        if qty < 1:
            raise ValueError("Quantity must be at least 1")

        if product.sku in self._items:
            self._items[product.sku].qty += qty
        else:
            self._items[product.sku] = CartItem(product, qty)

    def remove(self, sku: str) -> None:

        if sku not in self._items:
            raise KeyError("Product not found in cart")

        del self._items[sku]

    def subtotal(self) -> float:

        return sum(item.subtotal() for item in self._items.values())

    def total(self) -> float:

        subtotal = self.subtotal()
        return self.strategy.calculate(subtotal)