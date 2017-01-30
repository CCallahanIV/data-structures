"""Implement an insertion sort algorithm."""

import sys


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
            print(timeit.timeit("insertion_sort(test_lists[i])", setup="from __main__ import insertion_sort")
