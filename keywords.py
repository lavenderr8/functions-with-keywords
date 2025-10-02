def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def test_max_number():
    assert max_number(1, -1) == 1, "Ошибка: из чисел (1, -1) наибольшее будет 1."
    assert max_number(1, 1) == 1, "Ошибка: из чисел (1, 1) наибольшее должно быть 1."
    assert max_number(4, 8) == 8, "Ошибка: из чисел (4, 8) наибольшее будет 8."
    assert max_number(6, 2) == 6, "Ошибка: из чисел (4, 6) наибольшее будет 6."


test_max_number()
