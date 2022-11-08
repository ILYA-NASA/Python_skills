# работа с ФАЙЛАМИ

# # запись
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('colors')
# data.close()

# # перезапись (конструкция виз/ас)
# with open('file.txt', 'w') as data:
#     data.writelines(colors)

# чтение
# path = 'file.txt'
# with open('file.txt', 'r') as data:
#     for _ in data:
#         print(_)
# data.close()


# импорт модуля
# from lec import f

# print(f(1))


# # ФУНКЦИИ def
# def new_string(simbol, count=3):
#     return simbol*count
# print(new_string('@'))
# print(new_string(2))


# def concatenation(*params):
#     res: str = ""  # переменной res указан тип данных
#     for item in params:
#         res += item
#     return res
# print(concatenation('a', 'b', 'c'))


# # РЕКУРСИЯ
# # на примере фибоначчи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# result_list = []
# for i in range(1, 10):
#     result_list.append(fib(i))
# print(result_list)


# # КОРТЕЖИ (tuple)
# a = (3, 2) # дополнительно присваивать, изменять или удалять значения из картежа нельзя
# print(a)
# print(a[-1]) # срез применим для кортежа (как и для любой другой последовательности)


# # СЛОВАРИ {dict}
# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →


# МНОЖЕСТВА {set}
a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a))  # set
print(type(b))  # set

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a))  # set
print(type(b))  # set
print(type(c))  # set
a = {1, 1, 1, 1, 1}
print(a)  # {1}

colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red')
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red')  # ok
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { }
print(colors)  # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)  # i = {8, 2, 5}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)  # frozenset({1, 2, 3, 5, 8})


# СПИСКИ [list]
list1 = [1, 2, 3, 4, 5]

print(len(list1))
print(list1)
print(list1.pop()) # метод pop извлеает последний элемент последовательности (или элемент индекса в скобках)
# print(list1)
# print(list1.pop())
# print(list1)

print(list1)
print(list1.insert(1, 11)) # метод insert добавляет элемент в последовательность
print(list1)

print(list1.append(11)) # метод append добавляет элемент в конец последовательности
print(list1)