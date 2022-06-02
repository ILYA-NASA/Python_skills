from os import system
system('cls')

# def to_bool(x):
#     if x == 0:
#         return False
#     return True

# def Ex2():
#     # ¬(X ⋁ Y ) = ¬X ⋀ ¬Y
#     for ix in range(2):
#         for iy in range(2):
#             x = to_bool(ix)
#             y = to_bool(iy)
#             if not (not(x or y) == (not(x) and not(y))) :
#                 return False
#     return True


# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

def request_user(f):
    user = False
    count = 1
    while f > 0:
        # if user == True:
        #     bot()
        user_request = int(
            input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        while user_request > 28:
            print(f'Игрок {int(user)+1} повторите ввод!')
            user_request = int(
                input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        f -= user_request
        print(f)
        count += 1
        user = not(user)
        if f == 0:
            print(f'Игрок {int(user)+1} победил!')


def bot(f):
    return (f % 29) - 1


full = 100
request_user(full)