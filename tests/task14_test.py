from tasks import task14

assert (list(task14.my_map(abs, [-1, 2, -3]))) == [1, 2, 3]

assert list(task14.my_filter(lambda x: x % 2 == 1, range(10))) == [1, 3, 5, 7, 9]

assert (list(task14.replicate_each(3, [1, 'a']))) == [1, 1, 1, 'a', 'a', 'a']
