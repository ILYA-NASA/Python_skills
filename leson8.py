# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. 
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

# def find_info(name, age, city):
#     str_info = f'{name}, {age} год(а), проживает в городе {city}'
#     return str_info

# user_name = 'Василий'
# user_age = 21
# user_city = 'Москва'
# print(find_info(user_name, user_age, user_city))


# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

# print(max(2,1,4))


# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. 
# ### Поэкспериментируйте со значениями урона и жизней по желанию. 
# ### Теперь надо создать функцию attack(person1, person2). 
# Примечание: имена аргументов можете указать свои. 
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
# Функция должна сама работать со словарями и изменять их значения.

# player = {'name': input('Enter players name: '), 'health': 100, 'damage': 30}
# enemy = {'name': input('Enter enemys name: '), 'health': 100, 'damage': 20}

# def attack(person1, person2):
#     person2['health'] = person2.get('health') - person1.get('damage')
#     return person1, person2

# print(attack(player, enemy))

# 4: Давайте усложним предыдущее задание. 
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон 
# по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
# Примечание. 
# Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа. 

player = {'name': input('Enter players name: '), 'health': 100, 'damage': 30, 'armor': 1.2}
enemy = {'name': input('Enter enemys name: '), 'health': 100, 'damage': 20, 'armor': 1.2}

def split_damage(person1):
    person1['damage'] = person1.get('damage') / person1.get('armor')
    return person1

def attack(person1, person2):
    person2['health'] = person2.get('health') - split_damage(person1).get('damage')
    return person1, person2

print(attack(player, enemy))