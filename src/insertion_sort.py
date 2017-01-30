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


def filled_list():
    """Return a list of random numbers from 0 to 300 of random size less than 300."""
    import random
    a = random
    b = random
    c = a.randint(0, 300)
    return b.sample(range(0, 300), c)


l = filled_list()


if __name__ == "__main__":
    import timeit
    insertion_sort_timed = timeit.repeat(stmt="insertion_sort(l)", setup="from insertion_sort import insertion_sort, l", number=1000, repeat=3)
    average_insertion_sort_timed = float(sum(insertion_sort_timed) / len(insertion_sort_timed))

    print("number of runs: " + str(3))
    print("insertion_sort_timed: " + str(insertion_sort_timed))
    print("average: ", str(average_insertion_sort_timed))
