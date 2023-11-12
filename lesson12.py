from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float


@dataclass
class Pizza(Product):
    added: str
    hot: bool
    diameter: float


@dataclass
class Coffee(Product):
    V: float
    type: str


class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        """Позволяет создать товар"""

    @abstractmethod
    def sell_product(self, product: Product):
        """Позволяет продать товар"""

    @abstractmethod
    def all_products(self) -> list[Product]:
        """Выводит перечен всех товаров"""


class RealShop(AbstractShop):
    def __init__(self):
        self.list: list = []

    def add_product(self, product: Product):
        self.list.append(product)

    def sell_product(self, product: Product):
        self.list.remove(product)

    def all_products(self):
        return self.list


shop = RealShop()
a = Product(1, 'food', 1.0)
shop.add_product(a)
print(shop.all_products())
shop.sell_product(a)
print(shop.all_products())
b = Pizza(2, 'margarita', 10.0, 'cheese', False, 3.5)
shop.add_product(b)
print(shop.all_products())
shop.sell_product(b)
print(shop.all_products())
c = Coffee(3, 'latte', 3.45, 300, 'latte')
shop.add_product(c)
print(shop.all_products())
shop.sell_product(c)
print(shop.all_products())


class Error(ValueError):
    pass


def cheker(product: Product):
    if not isinstance(product, Product):
        raise Error('NonProductError')


furniture_shop = RealShop()


@dataclass
class Furniture(Product):
    price: float
    m: float
    id: int


@dataclass
class Chair(Furniture):
    color: str
    back: bool


@dataclass
class Table(Furniture):
    material: str
    height: float
    width: float


@dataclass
class Wardrobe(Furniture):
    doors: int
    mirror: bool


def furniture_checker(product: Furniture):
    if not isinstance(product, Furniture):
        raise Error('NonProductError')
