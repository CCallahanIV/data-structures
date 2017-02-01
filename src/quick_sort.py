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
quick_sort:
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


# def _random_list():
#     """Return a list of random numbers from 0 to 300 of size 150."""
#     import random
#     b = random
#     return b.sample(range(0, 300), 150)


# a = _random_list()
# r = a[:]
# b = sorted(a)
# w = b[::-1]


# if __name__ == "__main__":
#     import timeit

#     random_quick_sort_timed = timeit.repeat(stmt="quick_sort(r)", setup="from quick_sort import quick_sort, r", number=1000, repeat=3)
#     random_average_quick_sort_timed = float(sum(random_quick_sort_timed) / len(random_quick_sort_timed))

#     print("number of runs: " + str(3))
#     print("random quick_sort_timed: " + str(random_quick_sort_timed))
#     print("average: ", str(random_average_quick_sort_timed))

#     best_quick_sort_timed = timeit.repeat(stmt="quick_sort(b)", setup="from quick_sort import quick_sort, b", number=1000, repeat=3)
#     best_average_quick_sort_timed = float(sum(best_quick_sort_timed) / len(best_quick_sort_timed))

#     print("number of runs: " + str(3))
#     print("best case quick_sort_timed: " + str(best_quick_sort_timed))
#     print("average: ", str(best_average_quick_sort_timed))

#     worst_quick_sort_timed = timeit.repeat(stmt="quick_sort(w)", setup="from quick_sort import quick_sort, w", number=1000, repeat=3)
#     worst_average_quick_sort_timed = float(sum(worst_quick_sort_timed) / len(worst_quick_sort_timed))

#     print("number of runs: " + str(3))
#     print("worst case quick_sort_timed: " + str(worst_quick_sort_timed))
#     print("average: ", str(worst_average_quick_sort_timed))
