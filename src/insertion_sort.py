"""Implement an insertion sort algorithm."""

import sys
import timeit
from random import randint


def insertion_sort(sort_list):
    """Return a sorted list using the insertion sort algorithm."""
    pass


if __name__ == '__main__':
    if sys.argv[1]:
        result = insertion_sort(sys.argv[1])
        print("Sorted list: ", result)
    else:
        test_list1 = []
