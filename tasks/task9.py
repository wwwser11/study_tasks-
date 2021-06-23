# 9. Реализуйте аналог функций zip, map, enumerate.

def my_zip(*args):
    list_of_length = []
    list2 = []
    final_list = []
    for i, char in enumerate(args):
        list_of_length.append(len(char))
    min_length = min(list_of_length)
    for i in range(min_length):
        list2.clear()
        for j, char in enumerate(args):
            list2.append(char[i])
        final_list.append(tuple(list2.copy()))
    return final_list


def my_map(func, *iterables):
    list_of_length = []
    for i, char in enumerate(iterables):
        list_of_length.append(len(char))
    min_length = min(list_of_length)
    list_of_args = iterables
    for i in range(min_length):
        a = [item[i] for item in list_of_args]
        func()






l1 = [1, 2, 3]
l2 = [4, 5, 6]
# print(hasattr(l2, '__iter__'))

new_list = list(my_map(lambda x, y: x + y, l1, l2))
print(new_list)

a = [1,2,3]
b = "xyz"
c = (None, True)

print(my_zip(a, b, c))
