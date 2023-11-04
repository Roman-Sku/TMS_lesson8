# 1
class Auto:
    def __init__(self, brand: str, age: int, mark: str, color='', weight=''):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @staticmethod
    def move():
        return 'move'

    @staticmethod
    def stop():
        return 'stop'

    def birthday(self):
        self.age += 1
        return self.age


# 2
class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_load: int):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        super().move()
        return '!attention! move'


    @staticmethod
    def load():
        import time
        return time.sleep(1), 'load', time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: int):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'move', f'max speed is {self.max_speed}')


truck1 = Truck('Ford', 25, '1234', 1750)
print(truck1.load())
print(truck1.move())
print(truck1.stop())
print(truck1.birthday())
print('==========================================')
truck2 = Truck('Volvo', 2, 'xc90', 2000)
print(truck2.load())
print(truck2.move())
print(truck2.stop())
print(truck2.birthday())
print('==========================================')
car1 = Car('Audi', 1, 'rs6', 370)
print(car1.move())
print(car1.birthday())
print(car1.stop())
print('==========================================')
car2 = Car('Cirroen', 1, 'c5', 1000)
print(car2.move())
print(car2.birthday())
print(car2.stop())
