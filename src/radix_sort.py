"""Implement an insertion sort algorithm."""

import sys
from queue_ds import Queue


def radix_sort(sort_list):
    """Return a sorted list using the radix sort algorithm."""
    buckets = {char: Queue() for char in list('0123456789')}
    max_digits = 0
    digit = -1
    while True:
        for item in sort_list:
            try:
                buckets[str(item)[digit]].enqueue(item)
                if len(str(item)) > max_digits:
                    max_digits = len(str(item))
            except IndexError:
                buckets['0'].enqueue(item)
        new_list = []
        for i in range(10):
            while len(buckets[str(i)]) > 0:
                new_list.append(buckets[str(i)].dequeue())
        if abs(digit) > max_digits:
            return new_list
        digit -= 1
        sort_list = new_list


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = radix_sort(list(sys.argv[1]))
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
            print(timeit.timeit("radix_sort(test_lists[i])", number=1000, setup="from __main__ import radix_sort", globals=globals()))
