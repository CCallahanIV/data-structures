"""Merge Sort Module."""

# MERGE SORT (MS)
#
# CodeFellows 401d5
# Submission Date:
#
# Authors:  Colin Lamont <https://github.com/chamberi>
#           Ben Shields <https://github.com/iamrobinhood12345>
#
# URL:


def merge_sort(msl):
    """Merge sort method."""
    if len(msl) == 1 or not msl:
        return msl
    msl1 = msl[:int(len(msl) / 2)]
    msl2 = msl[int(len(msl) / 2):]

    msl1 = merge_sort(msl1)
    msl2 = merge_sort(msl2)

    def _merge(msla, mslb):
        sorted_list = []
        while len(msla) and len(mslb):
            if msla[0] < mslb[0]:
                low = msla.pop(0)
            else:
                low = mslb.pop(0)
            sorted_list.append(low)
        if len(msla):
            sorted_list.extend(msla)
            return sorted_list
        else:
            sorted_list.extend(mslb)
            return sorted_list

    return _merge(msl1, msl2)


def _random_list():
    """Return a list of random numbers from 0 to 300 of random size less than 300."""
    import random
    b = random
    return b.sample(range(0, 300), 150)


def _best_list():
    """Return a list of random numbers of random size less than 300 in ascending order."""
    import random
    b = random
    return sorted(b.sample(range(0, 300), 150))


def _worst_list():
    """Return a list of randon numbers of random size less than 300 in descending order."""
    import random
    b = random
    return sorted(b.sample(range(0, 300), 150))[::-1]


r = _random_list()
b = _best_list()
w = _worst_list()


if __name__ == "__main__":
    import timeit

    random_merge_sort_timed = timeit.repeat(stmt="merge_sort(r)", setup="from merge_sort import merge_sort, r", number=1000, repeat=3)
    random_average_merge_sort_timed = float(sum(random_merge_sort_timed) / len(random_merge_sort_timed))

    print("number of runs: " + str(3))
    print("random merge_sort_timed: " + str(random_merge_sort_timed))
    print("average: ", str(random_average_merge_sort_timed))

    best_merge_sort_timed = timeit.repeat(stmt="merge_sort(b)", setup="from merge_sort import merge_sort, b", number=1000, repeat=3)
    best_average_merge_sort_timed = float(sum(best_merge_sort_timed) / len(best_merge_sort_timed))

    print("number of runs: " + str(3))
    print("best case merge_sort_timed: " + str(best_merge_sort_timed))
    print("average: ", str(best_average_merge_sort_timed))

    worst_merge_sort_timed = timeit.repeat(stmt="merge_sort(w)", setup="from merge_sort import merge_sort, w", number=1000, repeat=3)
    worst_average_merge_sort_timed = float(sum(worst_merge_sort_timed) / len(worst_merge_sort_timed))

    print("number of runs: " + str(3))
    print("worst case merge_sort_timed: " + str(worst_merge_sort_timed))
    print("average: ", str(worst_average_merge_sort_timed))
