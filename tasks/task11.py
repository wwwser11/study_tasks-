def non_empty_truths(some_list):
    return [
        i for i in
        [
            [y for y in x if y]
            for x in some_list if x
        ]
        if i
    ]


print(non_empty_truths([]))
print(non_empty_truths([[0, ""], [False, None], [False, None, 0, 0]]))
print(non_empty_truths([[0, 1, 2], [], [], [False, True, 42]]))
