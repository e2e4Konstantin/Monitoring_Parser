import os
from pprint import pprint


def get_file_list(directory):
    file_list = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_list.append(file)
    return file_list


directory = r"C:\Users\kazak.ke\Documents\Задачи\5_Надя\исходные_данные\мониторинг"
file_list = get_file_list(directory)
pprint(file_list)
