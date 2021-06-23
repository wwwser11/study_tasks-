# 3. Написать функцию, принимающую строку s и число n возвращающую всевозможные перестановки
# из n символов в s строке в лексикографическом порядке(использовать itertools.permutations)

from itertools import permutations


def mix_ur_string(s, n):
    return list(permutations(s, n))


print(mix_ur_string('abp', 3))
