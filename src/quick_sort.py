"""Quick Sort Module."""

# QUICK SORT (MS)
#
# CodeFellows 401d5
# Submission Date:
#
# Authors:  Colin Lamont <https://github.com/chamberi>
#           Ben Shields <https://github.com/iamrobinhood12345>
#
# URL:

"""
quick_sort: picks a pivot, compares the rest of list next to the pivot, creates a lesser and greater list, and recursively calls quick_sort, combining the sorted lists and initial pivot at the end.
"""


def quick_sort(sort_list):
    """Quick sort method."""
    if len(sort_list) == 1 or not sort_list:
        return sort_list
    pivot = sort_list[0]
    sort_list1 = []
    sort_list2 = []
    for item in sort_list[1:]:
        if item < pivot:
            sort_list1.append(item)
        else:
            sort_list2.append(item)
    sort_list1 = quick_sort(sort_list1)
    sort_list1.append(pivot)
    sort_list2 = quick_sort(sort_list2)
    return sort_list1 + sort_list2


def _random_list():
    """Return a list of random numbers from 0 to 300 of size 150."""
    import random
    b = random
    return b.sample(range(0, 300), 150)


a = _random_list()
r = a[:]
b = sorted(a)
w = b[::-1]


if __name__ == "__main__":
    import timeit

    random_quick_sort_timed = timeit.repeat(stmt="quick_sort(r)", setup="from quick_sort import quick_sort, r", number=1000, repeat=3)
    random_average_quick_sort_timed = float(sum(random_quick_sort_timed) / len(random_quick_sort_timed))

    print("number of runs: " + str(3))
    print("random quick_sort_timed: " + str(random_quick_sort_timed))
    print("average: ", str(random_average_quick_sort_timed))

    arranged_quick_sort_timed = timeit.repeat(stmt="quick_sort(b)", setup="from quick_sort import quick_sort, b", number=1000, repeat=3)
    arranged_average_quick_sort_timed = float(sum(arranged_quick_sort_timed) / len(arranged_quick_sort_timed))

    print("number of runs: " + str(3))
    print("arranged case quick_sort_timed: " + str(arranged_quick_sort_timed))
    print("average: ", str(arranged_average_quick_sort_timed))

    reversed_quick_sort_timed = timeit.repeat(stmt="quick_sort(w)", setup="from quick_sort import quick_sort, w", number=1000, repeat=3)
    reversed_average_quick_sort_timed = float(sum(reversed_quick_sort_timed) / len(reversed_quick_sort_timed))

    print("number of runs: " + str(3))
    print("reversed case quick_sort_timed: " + str(reversed_quick_sort_timed))
    print("average: ", str(reversed_average_quick_sort_timed))
