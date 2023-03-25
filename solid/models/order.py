from dataclasses import dataclass, field

from .base import Model
from .product import Product


@dataclass
class OrderLine(Model):
    product: Product
    qty: int = field(default=1)


@dataclass
class Order(Model):
    lines: list[OrderLine] = field(init=False)
    total_amount: float = field(init=False)

    def add_line(self, product: Product, qty: int):
        self.lines.append(OrderLine(product=product, qty=qty))
        self.total_amount = self.__calculate_total_amount()

    def __calculate_total_amount(self):
        """Calculate total amount from stored lines"""
        return sum(line.product.amount * line.qty for line in self.lines)
