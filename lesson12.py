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


class NonProductError(ValueError):
    pass


class RealShop(AbstractShop):
    def __init__(self):
        self.list: list = []

    def add_product(self, product: Product):
        self.checker(product)
        self.list.append(product)

    def sell_product(self, product: Product):
        self.checker(product)
        self.list.remove(product)

    def all_products(self):
        return self.list

    @staticmethod
    def checker(product: Product):
        if not isinstance(product, Product):
            raise NonProductError('Не является продуктом')


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


class FurnitureShop(AbstractShop):
    def __init__(self):
        self.list: list = []

    def add_product(self, furniture: Furniture):
        self.checker(furniture)
        self.list.append(furniture)

    def sell_product(self, furniture: Furniture):
        self.checker(furniture)
        self.list.remove(furniture)

    def all_products(self):
        return self.list

    @staticmethod
    def checker(furniture: Furniture):
        if not isinstance(furniture, Furniture):
            raise NonProductError('Не является продуктом')
