print('======================= 1 ======================')
numbers1 = [1, 2, 3, 4, 14, 16, 12, 11, 123]
new_numbers1 = list(filter(lambda number: number % 2 == 0, numbers1))
print(new_numbers1)

print('======================== 2 ==========================')
info = [('Max', 16), ('Bob', 20), ('Ann', 23)]
new_info = list[tuple](sorted(info, key=lambda x: x[1]))
print(new_info)

print('======================== 3 ==========================')
list1 = ['hello', 'interesting', 'world']
vowels = {'a', 'e', 'i', 'o', 'u'}
new_list = list[str](filter(lambda x: x[0] in vowels, list1))
print(new_list)

print('======================== 4 ==========================')
list1 = [1, 2, 3, 4]
new_list = list[int](map(lambda x: x ** 2, list1))
print(new_list)

print('======================== 5 ==========================')
list1 = ['Helo', 'intresting', 'world', '!']
new_list = list[str](sorted(list1, key=lambda x: len(x), reverse=True))
print(new_list)

print('======================== 6 ==========================')
str1 = 'Hello interesting world !'
python = {'p', 'y', 't', 'h', 'o', 'n'}
list1 = list[str](filter(lambda x: x in python, str1))
print(list1)

print('======================== 7 ==========================')


def x_10(list1: list[int]) -> list[int]:
    new_list = []
    for num in list1:
        num = num * 10
        new_list.append(num)
    return new_list


print(x_10([1, 2, 3, 4]))

print('======================== 8 ==========================')
list1 = ['bingo', 'integer', 'account']
new_list = list[str](sorted(list1))
print(new_list)

print('======================== 9 ==========================')
list1 = ['binib', 'integer', 'accocca']
new_list = list[str](filter(lambda x: x == x[::-1], list1))
print(new_list)

print('======================== 10 ==========================')
list1 = ['bingo', 'integer', 'account']
new_list = sorted(list1, key=lambda c, x: sum(for c in vowels))
print(new_list)

print('======================== 11 ==========================')
# list1 = ['binib', 'integer', 'accocca']
# new_list = list(map(lambda x: x.upper, list1))
# print(new_list)

print('======================== 12 ==========================')