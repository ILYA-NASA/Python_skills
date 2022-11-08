# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

from random import choice


new_list = [1, 2, 3, 4]
def rand_element(full_list):
    try:
        return choice(full_list)
    except:
        return None 

# print(rand_element(new_list))