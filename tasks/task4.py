# 4. Реализовать функцию get_combinations.
# Должна принимать строку s  и число k
# и возвращать все возможные комбинации
# из символов в строке s с длинами <= k (itertools.combinations)

from itertools import combinations


def get_combinations(s, k):
    return list(combinations(s, k))


print(combinations('absp', 3))