import my_lib
import pytest
# Тест функции, которая выводит первые "n" чисел Фибоначчи

    # Тест функции на коррктных данных.
def test_on_correct():
    assert my_lib.fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # Тест функции на некорретных данных.
def test_on_negative():
    with pytest.raises(IndexError):
        my_lib.fibonacci(-5)
