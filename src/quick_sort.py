"""Implement an insertion sort algorithm."""

import sys


def quick_sort(sort_list, first=None, last=None):
    """Return a sorted list using the quick sort algorithm."""
    if first is None and last is None:
        first = 0
        last = len(sort_list) - 1
    if first < last:
        split = partition(sort_list, first, last)
        quick_sort(sort_list, first, split - 1)
        quick_sort(sort_list, split + 1, last)
    return sort_list


def partition(lst, first, last):
    """Sort a portion of list with relation to the value at index first."""
    pivot = lst[first]
    left = first + 1
    right = last
    while True:
        while lst[left] <= pivot and left <= right:
            left += 1
        while lst[right] >= pivot and right >= left:
            right -= 1
        if left >= right:
            break
        else:
            lst[left], lst[right] = lst[right], lst[left]
    lst[left], lst[right] = lst[right], lst[left]
    return right

if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = quick_sort(list(sys.argv[1]))
        print("Sorted list: ", result)
    else:
        import timeit
        from random import randint
        test_list1 = [randint(0, 10) for i in range(10)]
        test_list2 = [randint(0, 100) for i in range(10)]
        test_list3 = [randint(0, 100) for i in range(100)]
        test_list4 = [randint(0, 1000) for i in range(100)]
        test_list5 = [randint(0, 100) for i in range(1000)]
        test_list6 = [randint(0, 1000) for i in range(1000)]
        test_lists = [test_list1, test_list2, test_list3,
                      test_list4, test_list5, test_list6]
        test_desc = ["[randint(0, 10) for i in range(10)]",
                     "[randint(0, 100) for i in range(10)]",
                     "[randint(0, 100) for i in range(100)]",
                     "[randint(0, 1000) for i in range(100)]",
                     "[randint(0, 100) for i in range(1000)]",
                     "[randint(0, 1000) for i in range(1000)]"]

        for i in range(len(test_lists)):
            print("Testing: ", test_desc[i])
            print(timeit.timeit("quick_sort(test_lists[i])", number=1000, setup="from __main__ import quick_sort", globals=globals()))
