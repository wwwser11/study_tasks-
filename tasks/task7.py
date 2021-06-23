
# 7. В функцию передается список списков. Нужно вернуть максимум. который достигает выражение
#    (a1*a1 + a2*a2 + an*an). Где ai -- максимальный элемент из iго списка.

from functools import reduce
from itertools import starmap


def func(big_list):
    return reduce(lambda x, y: x + y**2, [0] + list(starmap(max, big_list)))


list_of_lists = [[1, 2, 3], [2, 2], [0, 0, 1, 1, 2], [0, 0]]
print(func(list_of_lists))