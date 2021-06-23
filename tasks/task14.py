def my_map(f, xs):
    for char in (f(x) for x in xs):
        yield char


def my_filter(f, xs):
    for char in (x for x in xs if f(x)):
        yield char


def replicate_each(n, xs):
    for char in xs:
        for i in range(n):
            yield char
        # yield from (char for i in range(n))

