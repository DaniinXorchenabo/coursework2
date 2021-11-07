from abc import ABC, abstractmethod
from array import ArrayType, array

__all__ = ['ShellSort', 'HeapSort', 'QuickSort']


class BaseSort(ABC):

    @classmethod
    @abstractmethod
    def sort(cls, a: ArrayType):
        pass


class ShellSort(BaseSort, ABC):
    @classmethod
    def sort(cls, a: ArrayType):
        pass


class HeapSort(BaseSort, ABC):
    @classmethod
    def sort(cls, a: ArrayType):
        pass


class QuickSort(BaseSort, ABC):
    @classmethod
    def sort(cls, a: ArrayType):
        pass
