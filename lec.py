# print('hello world')


# типы данных и переменная
# int, float, boolean, str, list, None

# value = None
# print(type(value))
# print(type(a))
# print(type(b))
# value = 12345
# print(type(value))
# s = 'hello world'
# a = 123
# b = 1.23
# # print(s) # вывод строки
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = [1, 2.4, '3', 'hi']
# print(list)

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = float(input())
# print(a, '+', b, '=', a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')


# Арифметические операции
# +, -, *, /, %, //, **
# **, ___________________
# (), Сокращенные операции

# a = 1.3123123
# b = 3
# c = round(a * b, 10)
# print(c)

# a = 3
# a *= 5
# print(a)


# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 4 and 5 > 2
# print(a)

# троноe и больше сравнение
# a = 1
# b = 4
# c = 2
# d = 6
# print(a < b > c < d)

# коньюнкция (and)
# f = 1 > 0 and 0 < 1
# print(f)

# дизьюнкция (or)
# f = 1 > 0 or 0 > 1
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)


# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Enter name: ')
# if username == 'Mary':
#     print("Yes, it's MARY!")
# elif username == 'Marina':
#     print("Hello, MARINA!")
# elif username == 'Ilnar':
#     print("ILNAR is best!")
# else:
#     print('Hi,', username)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Enough!')
# print(inverted)


# for
# list = [1, 2, 3, 10, 4, 5]
# for i in list:
#     print(i**2)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwe - rty':
#     print(i)


# Работа со строками

from turtle import color


text = 'съешь еще этих мягких французcких булок'
# print(len(text)) # длина строки 39
# print('еще' in text) #True строка "еще" в тексте есть
# print(text.isdigit()) #False текст из строк, а не из цифр
# print(text.islower()) #True
# print(text.replace('еще', 'ЕЩЕ'))

# Срезы
# print(text[0])
# print(text[1])
# print(text[len(text)-1]) # print(text[len(text)]) - не верно
# print(text[-5])
# print(text[:])
# print(text[:2])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# print(text[2:9] + text[-5] + text[:2])


# help(text.istitle)


# Списки
## list = list

# # Базовые API работы со списками:
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# numbers = list(ran)
# print(type(ran))
# print(type(numbers))
# print(numbers)
# numbers[0] = 10
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)


# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') # del colors[0] # удалить элемент


# ФУНКЦИИ
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))