# 2. Написать функцию, принимающую 2 списка и возвращающую декартово произведение
# (использовать itertools.product)

from itertools import product


def combinations_of_sum(list1, list2):
    return list(product(list1, list2))


print(combinations_of_sum(['a', 'b', 'f'], [1, 3, 'd']))

