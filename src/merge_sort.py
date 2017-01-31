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
    a = random
    b = random
    c = a.randint(0, 300)
    return b.sample(range(0, 300), c)


def _best_list():
    """Return a list of random numbers of random size less than 300 in ascending order."""
    import random
    a = random
    b = random
    c = a.randint(0, 300)
    return b.sample(range(0, 300), c).sorted()



r = _random_list()
b = _best_list()
w = _worst_list()


if __name__ == "__main__":
    import timeit
    merge_sort_timed = timeit.repeat(stmt="merge_sort(l)", setup="from merge_sort import merge_sort, l", number=1000, repeat=3)
    average_merge_sort_timed = float(sum(merge_sort_timed) / len(merge_sort_timed))

    print("number of runs: " + str(3))
    print("merge_sort_timed: " + str(merge_sort_timed))
    print("average: ", str(average_merge_sort_timed))
