def max_number(a, b):
    if a < 0 or b < 0:
        return "Ошибка: отрицательное число не может быть больше."
    elif a == b:
        return f"Ошибка: из чисел ({a}, {b}) невозможно выбрать наибольшее."
    elif a > b:
        return a
    else:
        return b


def test_max_number():
    assert max_number(1, -1) == "Ошибка: отрицательное число не может быть больше."
    assert max_number(1, 1) == "Ошибка: из чисел (1, 1) невозможно выбрать наибольшее."
    assert max_number(4, 8) == 8
    assert max_number(6, 2) == 6


test_max_number()
print("Все тесты пройдены!")

print(max_number(1, -1))
print(max_number(1, 1))
print(max_number(4, 8))
print(max_number(6, 2))


def empty_function():
    pass


print('Функция определена, но пока ничего не делает.')


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


print(list(even_numbers(8)))

