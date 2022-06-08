# 33. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools as it


# def ratios_list(k):
#     ratios = [randint(0, 10) for i in range(k + 1)]
#     if ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios


# def polynom_list(cof, ratios):
#     op = ['*x^']*(cof-1) + ['*x']
#     polynom = [[a, b, c] for a, b, c in it.zip_longest(
#         ratios, op, range(cof, 1, -1), fillvalue='') if a != 0]
#     for x in polynom:
#         x.append(' + ')
#     polynom = list(it.chain(*polynom))
#     polynom[-1] = ' = 0'
#     return "".join(map(str, polynom)).replace(' 1*x', ' x')


# cof = randint(2, 5)
# ratios = ratios_list(cof)
# polynom = polynom_list(cof, ratios)
# print(polynom)

# with open('Polynom_33.txt', 'w') as data:
#     data.write(polynom)

# 35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найти его.

# def get_data_file(file_txt):
#     data = open(file_txt, 'r')
#     data_list = data.read() + ' '
#     data_list = list(map(int, data_list.split()))
#     data.close()
#     return data_list


# def find_number(d_list):
#     for i in range(len(d_list)-1):
#         if d_list[i+1] - d_list[i] > 1:
#             return d_list[i] + 1


# def add_number(numbers):
#     for i in range(len(numbers)-1):
#         if numbers[i+1] - numbers[i] > 1:
#             numbers.insert(i+1, numbers[i]+1)
#     return numbers


# print(get_data_file('task35.txt'))
# print(find_number(get_data_file('task35.txt')))


# 43. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# так
result_list = []
for i in my_list:
    if my_list.count(i) == 1:
        result_list.append(i)
print(result_list)

# или так
print([i for i in my_list if my_list.count(i) == 1])
