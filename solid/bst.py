from dataclasses import dataclass, field
from typing import Any


@dataclass
class Node:
    """Node object of a binary tree."""

    data: Any
    left: "Node" | None = field(init=False)
    right: "Node" | None = field(init=False)


def search(root: Node | None, data: Any) -> Node | None:
    """Search in binary tree

    :param root: root node of a binary tree or a sub tree
    :type root: Node | None
    :param data: data can be anything which can be compareable
    :type data: Any
    :return: returns a node which has the passed data. otherwise, returns the parent node.
    :rtype: Node | None
    """

    # root is null or data is present at root
    if root is None or root.data == data:
        return root

    # data is greater than root's data
    if root.data < data:
        return search(root.right, data)

    # data is smaller than root's data
    return search(root.left, data)


def insert(root: Node | None, data: Any) -> Node | None:
    """Insert into binary tree

    :param root: root node of a tree or a sub tree
    :type root: Node | None
    :param data: data can by any object which can be compareable
    :type data: Any
    :return: returns a root node of a binary tree
    :rtype: Node | None
    """

    # root is null or data is present at root
    if root is None:
        return Node(data=data)

    # data is greater than root's data
    if root.data < data:
        root.right = insert(root.right, data)
    # data is less than root's data
    elif root.data > data:
        root.left = insert(root.left, data)

    return root


def build(values: list[Any]):
    """Build a binary tree from values list

    :param values: list of values contains any value which can be compareable.
    :type values: list[Any]
    :return: a root node and a nodes list
    :rtype: tuple[Node | None, list[Node | None]]
    """
    if not values:
        return None

    mid_num = len(values) // 2
    node = Node(values[mid_num])
    node.left = build(values[:mid_num])
    node.right = build(values[mid_num + 1 :])
    return node


def print_pre_order(root: Node | None):
    if not root:
        return

    print(root.data)
    print_pre_order(root.left)
    print_pre_order(root.right)
