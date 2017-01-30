"""Implement an insertion sort algorithm."""

import sys
import timeit
from random import randint


def insertion_sort(sort_list):
    """Return a sorted list using the insertion sort algorithm."""
    for i in range(1, len(sort_list)):
        saved_value = sort_list[i]
        trailing_index = i - 1
        while trailing_index >= 0 and sort_list[trailing_index] > saved_value:
            sort_list[trailing_index + 1] = sort_list[trailing_index]
            trailing_index -= 1
        sort_list[trailing_index + 1] = saved_value
    return sort_list


if __name__ == '__main__':
    if sys.argv[1]:
        result = insertion_sort(sys.argv[1])
        print("Sorted list: ", result)
    else:
        test_list1 = []
