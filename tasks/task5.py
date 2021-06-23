# 5. Функция должна принимать строку s и число k
# и возвращать все возможные комбинации
# из символов в строке s с длинами = k
# с повторениями ( использовать itertools.combinations)

from itertools import combinations_with_replacement


def combinations_of_ur_string(s, k):
    return list(combinations_with_replacement(s, k))


print(combinations_of_ur_string('absp', 3))