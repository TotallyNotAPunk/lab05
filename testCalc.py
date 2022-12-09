import my_lib
import pytest

# Тест функции, которая производит математические операции

    # Тестируем умножение.
def test_multi():
    assert my_lib.calc(4, 5, '*') == 20
    # Тестируем деление.
def test_div():
    assert my_lib.calc(20, 5, '/') == 4
    # Тестируем сложение.
def test_add():
    assert my_lib.calc(3, 5, '+') == 8
    # Тестируем вычетание.
def test_sub():
    assert my_lib.calc(10, 5, '-') == 5
    # Тест функции на некорретных данных.
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_lib.calc(5, 0, '/')
