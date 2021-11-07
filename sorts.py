from abc import ABC, abstractmethod
from array import ArrayType, array

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
        return 43.8


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
