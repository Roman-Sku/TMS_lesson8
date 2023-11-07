class Soda:
    def __init__(self, name: str):
        self.name = name

    def show_my_drink(self):
        self.name = input('Введите название газировки: ')
        soda_list = ['cola', 'pepsi', 'sprite']
        added_to_soda = 'b119'
        if self.name in soda_list:
            return f'{self.name} и {added_to_soda}'
        else:
            return 'Обычная газировка'


soda1 = Soda('pepsi')
print(soda1.show_my_drink())
soda2 = Soda('cola')
print(soda2.show_my_drink())

# ================================ 2 =================================
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) == str:
            return 'Нужно вводить только числа!'
        elif self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.c:
            return 'Ура, можно построить треугольник!'
        elif self.a < 0 or self.c < 0 or self.c < 0:
            return 'С отрицательными числами ничего не выйдет!'
        elif self.a + self.b < self.c and self.b + self.c < self.a and self.a + self.c < self.c:
            return 'Жаль, но из этого треугольник не сделать'


triangle1 = TriangleChecker('asd', 4, 5)
print(triangle1.is_triangle())
triangle2 = TriangleChecker(3, 4, 5)
print(triangle2.is_triangle())
triangle3 = TriangleChecker(-1, 4, 5)
print(triangle3.is_triangle())
triangle4 = TriangleChecker(5, 4, 5)
print(triangle4.is_triangle())


class KgToPounds:
    def __init__(self, __kg: int):
        self.__kg = __kg

    def to_pounds(self):
        return f'{self.__kg}кг это {self.__kg * 2.44}футов'

    def set_kg(self, __kg: int):
        self.__kg = int(input('Введите новое значение: '))

    def get_kg(self):
        return self.__kg

    @property
    def setter_kg(self):
        self.__kg = int(input('Введите новое значение: '))
        return self.__kg

    @property
    def getter_kg(self):
        return self.__kg


example1 = KgToPounds(500)
print(example1.to_pounds())


class RealString:
    def __init__(self, a: str, b: str):
        self.a = a
        self.b = b

    def compare(self):
        if len(self.a) > len(self.b):
            return 'Первая строка больше'
        else:
            return 'Вторая строка больше'


str12 = RealString('Apple', 'Яблоко')
print(str12.compare())


class Rectangle:
    def __init__(self, width: int, heigh: int):
        self.width = width
        self.height = heigh

    def get_atr(self):
        return self.width, self.height

    def str(self):
        while self.height > 0:
            print(self.width * '*')
            self.height -= 1

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return 2 * self.width + 2 * self.height

    def is_square(self):
        return self.width == self.height


class Person:
    def __init__(self, name:str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def get_person_atr(self):
        return self.name, self.age, self.gender

    def str(self):
        return f'Имя: {self.name} Возраст: {self.age} Пол: {self.gender}'

    def get_name(self):
        return self.name

    @property
    def set_name(self, new_name):
        self.name = new_name
        return self.name

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return bool
        elif age <= 18:
            return bool

    @classmethod
    def create_from_string(cls):
        s = 'name-age-geneder'
        values = s.split('-')
        return values[0], values[1], [2]


example1 = Person('ваня-13-мужской')
print(example1.create_from_string())



