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
    if len(msl) == 1:
        return msl
    msl1 = msl[:int(len(msl) / 2)]
    msl2 = msl[int(len(msl) / 2):]

    msl1 = merge_sort(msl1)
    msl2 = merge_sort(msl2)

    def merge(msla, mslb):
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

    return merge(msl1, msl2)
