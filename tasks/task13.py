
def each2d(test, matrix):
    return all(all(test(x) for x in y) for y in matrix)


def some2d(test, matrix):
    return any(any(test(x) for x in y) for y in matrix)

def sum2d(test, matrix):
    return sum([sum([x for x in y if test(x)]) for y in matrix])



