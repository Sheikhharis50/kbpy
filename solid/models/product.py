from dataclasses import dataclass

from .base import Model


@dataclass
class Product(Model):
    name: str
    amount: float
