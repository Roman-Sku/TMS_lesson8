from dataclasses import dataclass
from abstract import Product


@dataclass
class MotherBoard(Product):
    pass


@dataclass
class GPU(Product):
    pass


@dataclass
class CPU(Product):
    pass


@dataclass
class PSU(Product):
    pass


@dataclass
class Book(Product):
    pictures: bool
    list_amount: int


@dataclass
class Magazine(Product):
    fashion: bool
