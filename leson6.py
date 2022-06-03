# Game of guess the number (guess of user)

import random

# # 1 version (while True)
# numder = random.randint(1, 100)
# # print(numder)
# while True:
#     user_number = int(input('Input number (1 - 100): '))
#     if numder == user_number:
#         print('You winner!')
#         break
#     elif numder < user_number: 
#         print('You number > hidden number')
#     else: 
#         print('You number < hidden number')


# # 2 version (+ attempts and leves)
# numder = random.randint(1, 100)
# # print(numder)
# user_number = None
# levels = {1: 10, 2: 5, 3: 3}
# level = int(input('Input level (1 - 3): '))
# count = 0
# max_count = levels[level]
# while user_number != numder:
#     count += 1
#     if count > max_count:
#         print('You looser!')
#         break
#     print(f'Attempt {count}')
#     user_number = int(input('Input number (1 - 100): '))
#     if numder < user_number: 
#         print('You number > hidden number')
#     elif numder > user_number: 
#         print('You number < hidden number')
# else:
#     print('You winner!')


# 3 version (+ input quantity, names users and winner name)
numder = random.randint(1, 100)
# print(numder)
user_number = None
count = 0

levels = {1: 10, 2: 5, 3: 3}
level = int(input('Enter level (1 - 3): '))

user_count = int(input('Enter quantity users: '))
users = []
for i in range(user_count):
    user_name = input('Enter name user {i}: ')
    users.append(user_name)
# print(users)

max_count = levels[level]
is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('All users - loosers!')
        break
    print(f'Attempt {count}')
    for user in users:
        print(f'Queue for {user}')
        user_number = int(input('Enter number (1 - 100): '))
        if user_number == numder:
            is_winner = True
            winner_name = user
            break
        elif numder < user_number: 
            print('You number > hidden number')
        else: 
            print('You number < hidden number')
else:
    print(f'Winner is {winner_name}!')


# Game of guess the number (computer guess)