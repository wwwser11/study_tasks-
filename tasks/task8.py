# 8. Напишите генератор, выводящий первые n чисел Фибоначи.

def fibonacci_gen(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, b + a


print(list(fibonacci_gen(10)))
