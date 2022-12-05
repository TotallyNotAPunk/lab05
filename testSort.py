import my_lib
import pytest
# Тест функции, которая проверяет, что значения во входном списке упорядочены от мин к макс
class TestIsOrdered:
    # Тест функции на упорядоченных от мин к макс значениях
    def test_on_ordered(self, ordered_example):
        array = [1, 3, 5, 7, 9]
        assert my_lib.bubbleSort(array) == [1, 3, 5, 7, 9]

    # Тест функции на неупорядоченных значениях
    def test_on_unordered(self, unordered_example):
        array = [9, 7, 5, 3, 1]
        assert my_lib.bubbleSort(array) == [1, 3, 5, 7, 9]

    # Тест функции на равных по величине значениях
    def test_on_equal(self, equal_example):
        array = [5, 5, 5, 5, 5]
        assert my_lib.bubbleSort(array) == [5, 5, 5, 5, 5]

    # Тест функции на некорретных данных.
    def test_on_string(self):
        with pytest.raises(TypeError):
            my_lib.bubbleSort("Error")
