import os
import re
from fastnumbers import try_int
from pprint import pprint


def get_file_list(directory: str):
    file_list = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_list.append(file)
    return file_list

def get_bumper(file_name: str) -> int:
    file_prefix = re.split(r"[\t\n\r\f\v\s]+", file_name)[0]
    return try_int(file_prefix, on_fail=0)




directory = r"Y:\Казак К.Э\от Амбросимова\2024_2018_4"
files = get_file_list(directory)

files.sort(key=get_bumper)
pprint(files[:5])

d = {get_bumper(file): file for file in files}

pprint(d)

