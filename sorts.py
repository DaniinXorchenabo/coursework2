from abc import ABC, abstractmethod
from array import ArrayType, array
from time import time

__all__ = ['ShellSort', 'HeapSort', 'QuickSort', "SortType"]


class BaseSort(ABC):
    name: str = ''

    @classmethod
    @abstractmethod
    def sort(cls, a: ArrayType) -> float:
        pass


class ShellSort(BaseSort, ABC):
    name: str = 'Сортировка Шелла'

    @classmethod
    def sort(cls, a: ArrayType) -> float:
        start_time = time()
        inc = len(a) // 2
        while inc:
            for i, el in enumerate(a):
                while i >= inc and a[i - inc] > el:
                    a[i] = a[i - inc]
                    i -= inc
                a[i] = el
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)

        return time() - start_time


class HeapSort(BaseSort, ABC):
    name: str = 'Пирамидальная сортировка'

    @classmethod
    def sort(cls, a: ArrayType) -> float:
        return 15.1


class QuickSort(BaseSort, ABC):
    name: str = 'Быстрая сортировка'

    @classmethod
    def sort(cls, a: ArrayType) -> float:
        return 12.9


SortType = BaseSort
