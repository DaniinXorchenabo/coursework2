from abc import ABC, abstractmethod
from array import array, ArrayType
from random import randint


__all__ = ['SortedArray', 'ReverseSortedArray', 'UnsortedArray']


class BaseArray(ABC):

    def __init__(self, len_):
        self.len = len_
        self._array = []
        self.create_array()
        self._array: ArrayType
        assert isinstance(self._array, ArrayType) is True

    @abstractmethod
    def create_array(self) -> None:
        pass

    @property
    def array(self) -> ArrayType:
        return array(self._array)


class SortedArray(BaseArray):

    def create_array(self):
        # Преобразуем в массив итератор от 0 до числа, равного заданной длине
        self._array = array(range(self.len))


class ReverseSortedArray(BaseArray):
    def create_array(self):
        # Преобразуем в массив итератор от числа, равного заданной длине до нуля
        self._array = array(range(self.len - 1, -1, -1))


class UnsortedArray(BaseArray):
    def create_array(self):
        # создаём итератор заданной длины из случайных элементов и превращаем его в массив
        self._array = array((randint(0, self.len) for _ in range(self.len)))