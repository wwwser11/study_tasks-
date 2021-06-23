# 6. Написать функцию, которая подсчитывает количество подряд идущих символов в строке
# (использовать itertools.groupby)

from itertools import groupby


def how_much_repeat(string):
    for key, group in groupby(string):
        yield key, len(list(group))


string1 = 'aaassseaschhhjh'
print(list(how_much_repeat(string1)))