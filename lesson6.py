# 1
def root(x: int):
    x = x ** 2
    return x


number = int(input('Введите число: '))
res = root(number)
print(res)


# 2
def is_even(n: int):
    boolean = n % 2 == 0
    return boolean


number = int(input('Введите число: '))
a = is_even(number)
print(a)


# 3
def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


a = int(input('Введите число: '))
print(factorial(a))


# 4
def reverse(s: str):
    s = s[::-1]
    return s


str_1 = str(input("Введите текст: "))
print(reverse(str_1))


# 5
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input('Введите число: '))
print(fibonacci(number))


# 6
def count_vowels(s: str):
    counter = 0
    for letter in s:
        if letter in 'аеёиоуыэюя':
            counter += 1
    return counter


string = str(input('Введите текст: '))
print(count_vowels(string))


# 7
def is_palindrome(s: str):
    boolean = s[::-1] == s
    return boolean


string = str(input("Введите текст: "))
print(is_palindrome(string))


# 8
def power(x: int, n: int):
    result = x ** n
    return result


num1 = int(input('Введите число "x" : '))
num2 = int(input('Введите число "n" : '))
print(power(num1, num2))


# 9
def is_anagram(s1: str, s2: str):
    s1_list = list(s1)
    s1_list.sort()
    s2_list = list(s2)
    s2_list.sort()
    return s1_list == s2_list


str1 = str(input())
str2 = str(input())
print(is_anagram(str1, str2))


# 10
def is_pangram(s: str):
    s_lower = s.lower()
    s_list = list(s_lower)
    s_list.sort()
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    alphabet_list = list(alphabet)
    alphabet_list.sort()
    return s_list.sort() == alphabet_list.sort()


string = str(input("Введите текст: "))
print(is_pangram(string))
