# Functional Programming Study Tasks

## Overview (English)

This repository contains a series of tasks designed to practice functional programming techniques in Python. Each task encourages the use of higher-order functions, iterators, and generators to solve problems without modifying original data structures unless specified.

## Tasks

1. **List Modification During Iteration**  
   Check if it is possible to modify a list while iterating through it.

2. **Cartesian Product**  
   Write a function that takes two lists and returns their Cartesian product using `itertools.product`.

3. **Permutations of String**  
   Write a function that takes a string `s` and an integer `n`, and returns all possible `n`-character permutations of `s` in lexicographic order, using `itertools.permutations`.

4. **Combinations with Length <= k**  
   Implement `get_combinations`. It should take a string `s` and an integer `k`, and return all possible combinations of characters in `s` with lengths <= `k` using `itertools.combinations`.

5. **Combinations of Length k with Repetitions**  
   Write a function that takes a string `s` and an integer `k`, and returns all possible combinations of characters in `s` with length `k`, allowing repetitions, using `itertools.combinations_with_replacement`.

6. **Count Consecutive Characters**  
   Implement a function to count consecutive characters in a string using `itertools.groupby`.

7. **Maximize Expression with Lists**  
   Write a function that takes a list of lists and returns the maximum value of the expression `(a1 * a1 + a2 * a2 + ... + an * an)`, where `ai` is the largest element in the i-th list.

8. **Fibonacci Generator**  
   Create a generator that outputs the first `n` Fibonacci numbers.

9. **Custom zip, map, and enumerate**  
   Implement simplified versions of the functions `zip`, `map`, and `enumerate`.

10. **Odds from Odds**  
    Implement a function `odds_from_odds()` that, for an input list of lists, returns a new list of lists with only the odd-indexed lists (1st, 3rd, etc.) and, within each, only the odd-indexed elements. Ensure that this is a functional solution and does not modify the original list.

    - Additionally, write a procedure `keep_odds_from_odds()` that modifies the input list in place, retaining only the odd-indexed lists and elements as described above.

11. **Non-Empty Truths**  
    Write `non_empty_truths()` which takes a list of lists and returns a copy of the input with all false elements (e.g., `False`, `0`, empty strings) removed, as well as any empty lists.

12. **Count Unique Letters**  
    Implement `number_of_unique_letters()` which counts the number of unique letters in a string, case-insensitive.

13. **Matrix Predicate Functions**  
    Write three functions that operate on a 2D matrix (a list of lists):

    - `each2d(test, matrix)`: Returns `True` if every element in `matrix` satisfies the predicate `test`; otherwise, returns `False`.
    - `some2d(test, matrix)`: Returns `True` if at least one element in `matrix` satisfies the predicate `test`; otherwise, returns `False`.
    - `sum2d(test, matrix)`: Returns the sum of all elements in `matrix` that satisfy the predicate `test`.

    Ensure that `each2d` and `some2d` stop processing as soon as the result is determined.

14. **Generator Functions**  
    Write three generator functions:

    - `my_map(f, xs)`: A simplified version of `map()`.
    - `my_filter(f, xs)`: A simplified version of `filter()`.
    - `replicate_each(n, xs)`: For each element in `xs`, output `n` copies of that element.

---

## Описание задач (Русский)

Этот репозиторий содержит задачи для тренировки навыков функционального программирования на Python. Каждая задача ориентирована на использование функций высшего порядка, итераторов и генераторов для решения задач без изменения исходных структур данных, если это не указано в условиях.

## Задачи

1. **Изменение списка при итерировании**  
   Проверьте, можно ли изменять список в процессе итерирования по нему.

2. **Декартово произведение**  
   Напишите функцию, которая принимает два списка и возвращает их декартово произведение, используя `itertools.product`.

3. **Перестановки из строки**  
   Напишите функцию, которая принимает строку `s` и число `n` и возвращает всевозможные перестановки из `n` символов строки `s` в лексикографическом порядке, используя `itertools.permutations`.

4. **Комбинации с длиной <= k**  
   Реализуйте `get_combinations`, принимающую строку `s` и число `k`, и возвращающую все возможные комбинации символов строки `s` с длинами <= `k` с помощью `itertools.combinations`.

5. **Комбинации длиной k с повторениями**  
   Напишите функцию, принимающую строку `s` и число `k`, и возвращающую все возможные комбинации длиной `k` с повторениями, используя `itertools.combinations_with_replacement`.

6. **Подсчет подряд идущих символов**  
   Реализуйте функцию для подсчета количества подряд идущих символов в строке, используя `itertools.groupby`.

7. **Максимизация выражения с вложенными списками**  
   Напишите функцию, которая принимает список списков и возвращает максимальное значение выражения `(a1 * a1 + a2 * a2 + ... + an * an)`, где `ai` — максимальный элемент из i-го списка.

8. **Генератор Фибоначчи**  
   Создайте генератор, который выводит первые `n` чисел Фибоначчи.

9. **Аналоги zip, map и enumerate**  
   Реализуйте упрощенные версии функций `zip`, `map` и `enumerate`.

10. **Четные из четных**  
    Напишите функцию `odds_from_odds()`, которая для входного списка списков возвращает новый список списков, содержащий только нечетные по порядку списки (первый, третий и т.д.), и в каждом из них — только нечетные по порядку элементы. Решение должно быть функциональным и не изменять оригинальный список.

    - Также реализуйте процедуру `keep_odds_from_odds()`, которая изменяет список-аргумент по месту, оставляя только нечетные по порядку списки и элементы.

11. **Истинные непустые элементы**  
    Реализуйте функцию `non_empty_truths()`, которая принимает список списков и возвращает копию входного списка без ложных элементов (например, `False`, `0`, пустые строки) и пустых списков.

12. **Подсчет уникальных букв**  
    Напишите функцию `number_of_unique_letters()`, которая подсчитывает количество уникальных букв в строке без учета регистра.

13. **Предикаты для матрицы**  
    Реализуйте три функции, работающие с двухмерной матрицей (список списков):

    - `each2d(test, matrix)`: Возвращает `True`, если каждый элемент матрицы `matrix` удовлетворяет предикату `test`, иначе `False`.
    - `some2d(test, matrix)`: Возвращает `True`, если хотя бы один элемент матрицы `matrix` удовлетворяет предикату `test`, иначе `False`.
    - `sum2d(test, matrix)`: Возвращает сумму всех элементов матрицы `matrix`, которые удовлетворяют предикату `test`.

    Обратите внимание, что `each2d` и `some2d` должны прекращать обход матрицы, как только результат становится ясен.

14. **Генераторные функции**  
    Реализуйте три генераторные функции:

    - `my_map(f, xs)`: упрощенная версия `map()`.
    - `my_filter(f, xs)`: упрощенная версия `filter()`.
    - `replicate_each(n, xs)`: для каждого элемента `xs` выдает `n` копий этого элемента.
