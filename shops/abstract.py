from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Product:
    id: int
    name: str
    price: float


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

