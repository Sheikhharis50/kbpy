from dataclasses import dataclass, field

import bst
from models.order import Order, OrderLine
from models.product import Product


@dataclass
class DB:
    order_tree: bst.Node | None = field(init=False)
    product_tree: bst.Node | None = field(init=False)

    def add_product(self, product: Product):
        self.product_tree = bst.insert(self.product_tree, product)


def menu() -> int:
    print(
        """
        Select command from following menu:
        1)  Create product
        2)  Create order
        0)  Exit
        """
    )
    return int(input("Enter command no: "))


def create_product():
    product = Product(
        name=input("Enter product name: "),
        amount=float(input("Enter product amount: ")),
    )
    DB.products.append(product)
    print(f"Product Created! => {product}")


def create_order():
    order = Order()
    while True:
        ...


def main():
    commands_map = {
        1: create_product,
        2: create_order,
        0: exit,
    }

    while True:
        command = menu()
        # execute command
        commands_map[command]()


if __name__ == "__main__":
    main()
