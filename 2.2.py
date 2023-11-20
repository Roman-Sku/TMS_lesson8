# 1
print('=================== 1 =================')
list1 = list(input('Введите числа: '))
i = 0
while i < len(list1):
    list1[i] = int(list1[i])
    i += 1
a = sum(list1)
print(a)

# 2
print('=================== 2 =================')
str1 = str(input('Введите предложение: '))
a = str1.count('а')
b = str1.count('е')
c = str1.count('и')
d = str1.count('о')
e = str1.count('у')
f = str1.count('ы')
g = str1.count('э')
h = str1.count('ю')
p = str1.count('я')
print(a + b + c + d + e + f + g + h + p)

# 3
print('=================== 3 =================')
text = input('Введите предложение: ')
words = text.split()
very_long_word = ''
i = 0
while i < len(words):
    if len(words[i]) > len(very_long_word):
        very_long_word = words[i]
    i += 1
print(very_long_word)

# 4
print('=================== 4 =================')
list1 = (input('Введите числа: '))
total_list1 = list1.split(' ')
i = 0
while i < len(total_list1):
    total_list1[i] = int(total_list1[i])
    i += 1
list2 = []
list3 = []
i = 0
while i < len(total_list1):
    if total_list1[i] % 2 == 0:
        list2.append(total_list1[i])
    else:
        list3.append(total_list1[i])
    i += 1
print(list2)
print(list3)
i = 0
while i < len(list2):
    list2[i] = list2[i] * 2
    i += 1
print(list2)
print(list3)
