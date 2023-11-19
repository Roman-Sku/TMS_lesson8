from abstract import AbstractShop, NonProductError
from products import *


class BooksShop(AbstractShop):
    def __init__(self):
        self.list: list = []

    def add_product(self, product: Book | Magazine):
        self.checker(product)
        self.list.append(product)

    def sell_product(self, product: Book | Magazine):
        self.checker(product)
        self.list.remove(product)

    def all_products(self):
        return self.list

    @staticmethod
    def checker(product: Book | Magazine):
        if not isinstance(product, Book | Magazine):
            raise NonProductError('Не является продуктом')


class PCShop(AbstractShop):
    def __init__(self):
        self.list: list = []

    def add_product(self, product: MotherBoard | GPU | CPU | PSU):
        self.checker(product)
        self.list.append(product)

    def sell_product(self, product: MotherBoard | GPU | CPU | PSU):
        self.checker(product)
        self.list.remove(product)

    def all_products(self):
        return self.list

    @staticmethod
    def checker(product: MotherBoard | GPU | CPU | PSU):
        if not isinstance(product, MotherBoard | GPU | CPU | PSU):
            raise NonProductError('Не является продуктом')