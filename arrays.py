from abc import ABC, abstractmethod
from array import array, ArrayType
from random import randint


__all__ = ['SortedArray', 'ReverseSortedArray', 'UnsortedArray', 'ArrayClassType']


class BaseArray(ABC):

    def __init__(self, len_):
        self.len = len_
        self._array = array([])
        self.create_array()
        self._array: ArrayType
        assert isinstance(self._array, ArrayType) is True

    @abstractmethod
    def create_array(self, start=0, len_diff=0) -> None:
        pass

    @property
    def array(self) -> ArrayType:
        return array(self._array)

    def create_new_array(self, new_len) -> 'BaseArray':
        new_arr = self.__class__(0)
        new_arr._array = self.array
        new_arr.create_array(new_len, new_len - self.len)
        new_arr.len = new_len
        return new_arr


class SortedArray(BaseArray):

    def create_array(self, start=0, len_diff=0):
        # Преобразуем в массив итератор от 0 до числа, равного заданной длине
        self._array = array(range(start, self.len + len_diff))


class ReverseSortedArray(BaseArray):
    def create_array(self, start=0, len_diff=0):
        # Преобразуем в массив итератор от числа, равного заданной длине до нуля
        self._array = array(range(self.len + len_diff - 1, start-1, -1))


class UnsortedArray(BaseArray):
    def create_array(self, start=0, len_diff=0):
        # создаём итератор заданной длины из случайных элементов и превращаем его в массив
        self._array = array((randint(0, self.len) for _ in range(start, self.len + len_diff)))


ArrayClassType = BaseArray
