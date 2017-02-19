"""Implement an insertion sort algorithm."""

import sys


def merge_sort(sort_list):
    """Return a sorted list using the merge sort algorithm."""
    if len(sort_list) <= 1:
        return sort_list

    left = sort_list[:len(sort_list) // 2]
    right = sort_list[len(sort_list) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    """Sort left and right, returns a list of the two merged."""
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = merge_sort(list(sys.argv[1]))
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
            print(timeit.timeit("merge_sort(test_lists[i])", number=1000, setup="from __main__ import merge_sort", globals=globals()))
