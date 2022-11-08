# Помните игру с конфетами из модуля "Математика и Информатика"? 
# Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

def sweet_game(player_move):
    user = False
    count = 1
    while player_move > 0:
        # if user == True:
        #     sweet_bot()
        user_request = int(input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        while user_request > 28:
            print(f'Игрок {int(user)+1} повторите ввод!')
            user_request = int(
                input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        player_move -= user_request
        print(player_move)
        count += 1
        user = not(user)
        if player_move == 0:
            print(f'Игрок {int(user)+1} победил!')


def sweet_bot(player_move):
    return (player_move % 29) - 1


sweet_game(100)
