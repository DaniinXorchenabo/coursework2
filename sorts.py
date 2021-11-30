from abc import ABC, abstractmethod
from array import ArrayType, array
from time import time
import random

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
        start_time = time()

        def _shift(a: ArrayType, index, l, r):

            def print_heap(*a, **k):
                pass

            if r > (ind2 := l + index * 2 + 1):
                if a[(ind1 := l + index * 2)] > a[ind2]:
                    if a[(ind := l + index)] < a[ind1]:
                        a[ind], a[ind1] = a[ind1], a[ind]
                        a = _shift(a, index * 2, l, r)
                        print_heap(a)
                        return a
                else:
                    if a[(ind := l + index)] < a[ind2]:
                        a[ind], a[ind2] = a[ind2], a[ind]
                        a = _shift(a, index * 2 + 1, l, r)
                        print_heap(a)
                        return a
            elif r > (ind1 := l + index * 2):
                if a[(ind := l + index)] < a[ind1]:
                    a[ind], a[ind1] = a[ind1], a[ind]
                    a = _shift(a, index * 2, l, r)
                    print_heap(a)
                    return a
            print_heap(a)
            return a

        def create_heap(a: ArrayType) -> ArrayType:
            a.insert(0, int(0))
            [_shift(a, i, 0, len(a)) for i in range(len(a) // 2 - 1, 0, -1)]
            return a

        def _sort_shift(a: ArrayType, min_el_index, next_index) -> None:
            # print(a)
            a[min_el_index], a[next_index] = a[next_index], a[min_el_index]
            # print(a)
            _shift(a, min_el_index, 0, next_index)
            return None

        def _heap_sort(a: ArrayType) -> ArrayType:
            [(_sort_shift(a, 1, i), print(i)) for i in range(len(a) - 1, 0, -1)]
            return a

        a = create_heap(a)
        a = _heap_sort(a)
        print(time() - start_time, len(a))
        return time() - start_time


class QuickSort(BaseSort, ABC):
    name: str = 'Быстрая сортировка'

    @classmethod
    def sort(cls, a: ArrayType) -> float:
        def quicksort(nums):
            if len(nums) <= 1:
                return nums
            else:
                q = random.choice(nums)
            l_nums = [n for n in nums if n < q]

            e_nums = [q] * nums.count(q)
            b_nums = [n for n in nums if n > q]
            return quicksort(l_nums) + e_nums + quicksort(b_nums)

        start_time = time()
        quicksort(a)
        return time() - start_time


SortType = BaseSort
