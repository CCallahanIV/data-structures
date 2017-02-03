"""Radix Sort Module."""

# RADIX SORT (MS)
#
# CodeFellows 401d5
# Submission Date:
#
# Authors:  Colin Lamont <https://github.com/chamberi>
#           Ben Shields <https://github.com/iamrobinhood12345>
#
# URL:

"""
radix_sort: sorts numbers by their 0-9 digits first, putting them in a list from lowest to highest. Next does the same for 10s (10-99), and so forth.
"""


def radix_sort(sort_list):
    """Radix sort method."""
    if len(sort_list) == 1 or not sort_list:
        return sort_list
    iters = len(str(max(sort_list))) - 1
    for i in range(iters + 1):
        temp_list = []
        num_pots = [[] for x in range(10)]
        for item in sort_list:
            try:
                num_pots[int(str(item)[-(i + 1)])].append(item)
            except:
                num_pots[0].append(item)
        for nums in num_pots:
            temp_list.extend(nums)
        sort_list = temp_list
        iters -= 1
    return temp_list


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

    random_radix_sort_timed = timeit.repeat(stmt="radix_sort(r)", setup="from radix import radix_sort, r", number=1000, repeat=3)
    random_average_radix_sort_timed = float(sum(random_radix_sort_timed) / len(random_radix_sort_timed))

    print("number of runs: " + str(3))
    print("random radix_sort_timed: " + str(random_radix_sort_timed))
    print("average: ", str(random_average_radix_sort_timed))

    arranged_radix_sort_timed = timeit.repeat(stmt="radix_sort(b)", setup="from radix import radix_sort, b", number=1000, repeat=3)
    arranged_average_radix_sort_timed = float(sum(arranged_radix_sort_timed) / len(arranged_radix_sort_timed))

    print("number of runs: " + str(3))
    print("arranged case radix_sort_timed: " + str(arranged_radix_sort_timed))
    print("average: ", str(arranged_average_radix_sort_timed))

    reversed_radix_sort_timed = timeit.repeat(stmt="radix_sort(w)", setup="from radix import radix_sort, w", number=1000, repeat=3)
    reversed_average_radix_sort_timed = float(sum(reversed_radix_sort_timed) / len(reversed_radix_sort_timed))

    print("number of runs: " + str(3))
    print("reversed case radix_sort_timed: " + str(reversed_radix_sort_timed))
    print("average: ", str(reversed_average_radix_sort_timed))
