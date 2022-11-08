# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, 
# прочитать из них информацию. И получить объект: словарь из предыдущего задания.

import json
import pickle


with open('group.json', 'r', encoding='utf-8') as f:
    print(json.load(f))

    
with open('group.pickle', 'rb') as f:
    print(pickle.load(f))