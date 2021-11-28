from abc import ABC
from typing import Type

from sorts import ShellSort, HeapSort, QuickSort, SortType
from arrays import SortedArray, UnsortedArray, ReverseSortedArray, ArrayClassType


class Worker(ABC):
    setup_count: int = 10
    sort_list: list[SortType] = [ShellSort, HeapSort, QuickSort]
    arrays_list: list[ArrayClassType] = [SortedArray, UnsortedArray, ReverseSortedArray]

    def __init__(self, setup_count: int):
        self.setup_count = setup_count

    def graphs(self, array_type: Type[ArrayClassType], start: int, end: int) \
            -> list[list[dict[int, float], SortType]]:
        """

        :param array_type: класс выбранного массива
        :param start: с какого начинать считать время сортировки
        :param end: максимальная длина сортируемого массива
        :return:
        """
        _iter = self._get_iterator(start, end, self.setup_count)
        arrays: dict[float, ArrayClassType] = {-1: array_type(0)}
        for i in _iter:
            arrays[i] = arrays[-1].create_new_array(i)
        arrays.pop(-1)
        return [[self._graph(sort_type, arrays), sort_type] for sort_type in self.sort_list]

    @staticmethod
    def _graph(sort_type: SortType, array_type: dict[float, ArrayClassType]) -> dict[int, float]:
        """

        :param sort_type: тип сортировки
        :param array_type: тип массива
        :return: словарь, где ключ - количество элементов в массиве, а значение - время сортировки
        """
        return {iter_count: sort_type.sort(arr.array) for iter_count, arr in array_type.items()}

    @staticmethod
    def _get_iterator(start: int, end: int, setup_count: int):
        return range(start, end, (end - start) // setup_count)
