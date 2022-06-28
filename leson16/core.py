# функция для создания файла
import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(massage):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {massage}'
    # print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    # create_file('text.dat')
    # create_file('text.dat', 'some text')
    # create_folder('new_f1')
    # get_list()
    # get_list(True)
    # delete_file('new_f')
    # delete_file('new2')
    # delete_file('text.dat')
    # delete_file('text2.dat')
    # delete_file('log.txt')
    delete_file('__pycache__')
    # copy_file('new_f', 'new2')
    # copy_file('text.dat', 'text2.dat')
    # save_info('massage')
