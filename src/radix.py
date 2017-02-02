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
radix_sort: picks a pivot, compares the rest of list next to the pivot, creates a lesser and greater list, and recursively calls radix_sort, combining the sorted lists and initial pivot at the end.
"""


def radix_sort(sort_list):
    """Radix sort method."""
    if len(sort_list) == 1 or not sort_list:
        return sort_list
    temp_dict, new_dict, last_dict = {}, {}, {}
    temp_list, new_list, last_list = [], [], []
    for item in sort_list:
        import pdb; pdb.set_trace()
        temp_dict.setdefault(int(str(item)[2]), [])
        temp_dict[int(str(item)[2])].append(item)
    for key, value in temp_dict.items():
        temp_list.extend(value)
    for item in temp_list:
        new_dict.setdefault(int(str(item)[1]), [])
        new_dict[int(str(item)[1])].append(item)
    for key, value in new_dict.items():
        new_list.extend(value)
    for item in new_list:
        last_dict.setdefault(int(str(item)[0]), [])
        last_dict[int(str(item)[0])].append(item)
    for key, value in last_dict.items():
        last_list.extend(value)
    return last_list

    # pivot = sort_list[0]
    # sort_list1 = []
    # sort_list2 = []
    # for item in sort_list[1:]:
    #     if item < pivot:
    #         sort_list1.append(item)
    #     else:
    #         sort_list2.append(item)
    # sort_list1 = radix_sort(sort_list1)
    # sort_list1.append(pivot)
    # sort_list2 = radix_sort(sort_list2)
    # return sort_list1 + sort_list2


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

#     random_radix_sort_timed = timeit.repeat(stmt="radix_sort(r)", setup="from radix_sort import radix_sort, r", number=1000, repeat=3)
#     random_average_radix_sort_timed = float(sum(random_radix_sort_timed) / len(random_radix_sort_timed))

#     print("number of runs: " + str(3))
#     print("random radix_sort_timed: " + str(random_radix_sort_timed))
#     print("average: ", str(random_average_radix_sort_timed))

#     arranged_radix_sort_timed = timeit.repeat(stmt="radix_sort(b)", setup="from radix_sort import radix_sort, b", number=1000, repeat=3)
#     arranged_average_radix_sort_timed = float(sum(arranged_radix_sort_timed) / len(arranged_radix_sort_timed))

#     print("number of runs: " + str(3))
#     print("arranged case radix_sort_timed: " + str(arranged_radix_sort_timed))
#     print("average: ", str(arranged_average_radix_sort_timed))

#     reversed_radix_sort_timed = timeit.repeat(stmt="radix_sort(w)", setup="from radix_sort import radix_sort, w", number=1000, repeat=3)
#     reversed_average_radix_sort_timed = float(sum(reversed_radix_sort_timed) / len(reversed_radix_sort_timed))

#     print("number of runs: " + str(3))
#     print("reversed case quick_sort_timed: " + str(reversed_quick_sort_timed))
#     print("average: ", str(reversed_average_quick_sort_timed))
