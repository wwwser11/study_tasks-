l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def odds_from_odds(input):
    numbers = []
    list_o = []
    for i in range(0, len(input), 2):
        for j in range(0, len(input[i]), 2):
            list_o.append(input[i][j])
        numbers.append(list_o.copy())
        list_o.clear()
    return numbers


def keep_odds_from_odds(input):
    for i in input[::2]:
        i[:] = i[::2]
    input[:] = input[::2]


print(odds_from_odds([]))
print(odds_from_odds(l))
keep_odds_from_odds(l)
print(l)
