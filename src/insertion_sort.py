"""Insertion Sort Module."""

# INSERTION SORT (IS)
#
# CodeFellows 401d5
# Submission Date:
#
# Authors:  Colin Lamont <https://github.com/chamberi>
#           Ben Shields <https://github.com/iamrobinhood12345>
#
# URL:


def insertion_sort(isl):
    """Insertion sort method."""
    for item in range(len(isl)):
        x = isl[item]
        neighbor = item - 1
        while neighbor >= 0 and isl[neighbor] > x:
            isl[neighbor + 1] = isl[neighbor]
            neighbor -= 1
        isl[neighbor + 1] = x
    return isl


def _random_list():
    """Return a list of random numbers from 0 to 300 of random size less than 300."""
    import random
    b = random
    return b.sample(range(0, 300), 150)


a = _random_list()
r = a[:]
b = sorted(a)
w = b[::-1]


if __name__ == "__main__":
    import timeit

    random_insertion_sort_timed = timeit.repeat(stmt="insertion_sort(r)", setup="from insertion_sort import insertion_sort, r", number=1000, repeat=3)
    random_average_insertion_sort_timed = float(sum(random_insertion_sort_timed) / len(random_insertion_sort_timed))

    print("number of runs: " + str(3))
    print("random insertion_sort_timed: " + str(random_insertion_sort_timed))
    print("average: ", str(random_average_insertion_sort_timed))

    best_insertion_sort_timed = timeit.repeat(stmt="insertion_sort(b)", setup="from insertion_sort import insertion_sort, b", number=1000, repeat=3)
    best_average_insertion_sort_timed = float(sum(best_insertion_sort_timed) / len(best_insertion_sort_timed))

    print("number of runs: " + str(3))
    print("best case insertion_sort_timed: " + str(best_insertion_sort_timed))
    print("average: ", str(best_average_insertion_sort_timed))

    worst_insertion_sort_timed = timeit.repeat(stmt="insertion_sort(w)", setup="from insertion_sort import insertion_sort, w", number=1000, repeat=3)
    worst_average_insertion_sort_timed = float(sum(worst_insertion_sort_timed) / len(worst_insertion_sort_timed))

    print("number of runs: " + str(3))
    print("worst case insertion_sort_timed: " + str(worst_insertion_sort_timed))
    print("average: ", str(worst_average_insertion_sort_timed))
