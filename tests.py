from array import array

from sorts import ShellSort, QuickSort, HeapSort
from arrays import SortedArray, UnsortedArray, ReverseSortedArray

sorted_array = SortedArray(10)
unsorted_array = UnsortedArray(10)
reverse_sorted = ReverseSortedArray(10)

print("\n\nСортировка Шелла")
print('Отсортированный массив:', list(sorted_array.array))
print("Результат сортировки:", list(ShellSort._sort(sorted_array.array)))
print('неотсортированный массив:', list(unsorted_array.array))
print("Результат сортировки:", list(ShellSort._sort(unsorted_array.array)))
print('массив, отсортированный в обратном порядке:', list(reverse_sorted.array))
print("Результат сортировки:", list(ShellSort._sort(reverse_sorted.array)))

print("\n\nПирамидальная сортировка")
print('Отсортированный массив:', list(sorted_array.array))
print("Результат сортировки:", list(HeapSort._sort(sorted_array.array)))
print('неотсортированный массив:', list(unsorted_array.array))
print("Результат сортировки:", list(HeapSort._sort(unsorted_array.array)))
print('массив, отсортированный в обратном порядке:', list(reverse_sorted.array))
print("Результат сортировки:", list(HeapSort._sort(reverse_sorted.array)))

print("\n\nБыстрая сортировка")
print('Отсортированный массив:', list(sorted_array.array))
print("Результат сортировки:", list(QuickSort._sort(sorted_array.array)))
print('неотсортированный массив:', list(unsorted_array.array))
print("Результат сортировки:", list(QuickSort._sort(unsorted_array.array)))
print('массив, отсортированный в обратном порядке:', list(reverse_sorted.array))
print("Результат сортировки:", list(QuickSort._sort(reverse_sorted.array)))
