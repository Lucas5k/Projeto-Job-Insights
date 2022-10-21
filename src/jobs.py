from functools import lru_cache
import csv


@lru_cache
def read(path: str):
    with open(path, encoding="utf8") as file:
        all_file = csv.DictReader(file, delimiter=',', quotechar='"')
        my_list = []
        for value in all_file:
            my_list.append(value)
    return my_list
