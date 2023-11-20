# 1
def make_sentence(words=None) -> str:
    if words is None:
        words = ["This", "is", "a", "sentence"]
    sentence_1 = ' '.join(words)
    return sentence_1 + '.'


print(make_sentence(['Python', 'is', 'fun']))


# 2
def sum_of_squares(*numbers: int) -> int:
    res = 0
    if len(numbers) == 0:
        return 0
    for number in numbers:
        res += number ** 2
    return res


print(sum_of_squares(1, 2, 3))


# 3
def greet(name: str, language='en'):
    if language == 'en':
        return f'Hello, {name}!'
    if language == 'ru':
        return f'Привет, {name}!'
    if language == 'fr':
        return f'Bonjour, {name}!'


print(greet('Igor', 'fr'))


# 4
def print_info(**kwargs):
    if not kwargs:
        return 'No info given'
    for key in kwargs.keys():
        print(f'{key}: {kwargs[key]}')


print_info(name='Alex', age=25, city='Amsterdam')


# 5
def print_table(**kwargs):
    if len(kwargs) == 0:
        print("No data given.")
        return
    print(f"|{'Key':<5}|{'Value':<10}|")
    print('|' + "-" * 16 + '|')
    for key, value in kwargs.items():
        print(f"|{key:<5}|{value:<10}|")


print_table(name='bob', age=30, city='Amsterdam')


# 6
def calculate(*args: int, operation='+'):
    if not args:
        return 0
    if operation == "+":
        print(sum(args))
    elif operation == "-":
        res = args[0]
        if len(args) == 1:
            print(res)
            return
        for number in args[1:]:
            res -= number
        print(res)
    elif operation == "*":
        res = 1
        for number in args:
            res *= number
        print(res)
    elif operation == "/":
        res = 1
        if len(args) == 1:
            print(res)
            return
        for number in args[1:]:
            res /= number
        print(res)


calculate(1, 2, 3, operation='*')


# 7
def print_triangle(height=5):
    a = 1
    for index in range(height):
        print(f"{'*' * a:^{height * 2}}")
        a += 2


print_triangle(height=4)


# 8
def create_post(title, text, author, category="general"):
    post = {
        "title": title,
        "text": text,
        "author": author,
        "category": category
    }
    return post


print(create_post(title='Концерт', text='Все песни', author='Михаил Круг'))


# 9
def create_product(name, price, category, rating=0):
    product = {
        "name": name,
        "price": price,
        "category": category,
        "rating": rating
    }
    return product


print(create_product(name='Кисель', price='2$', category='food',))
