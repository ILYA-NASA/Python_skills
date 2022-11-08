# ГЕНЕРАТОР СПИСКОВ
# Создать список из случайных чисел от 1 до 100
from random import randint
print([randint(1, 100) for i in range(10)])

# Список квадратов чисел
print([i**2 for i in [1,2,3, -4]])

# Список имн на букву А
# name_list = ['Альберт', 'Петр', 'Антон']
print([i for i in ['Альберт', 'Петр', 'Антон'] if i.startswith('А')])