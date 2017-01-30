"""Insertion Sort Module."""


def insert_sort(isl):
    """Insertion sort method."""
    for item in range(len(isl)):
        x = isl[item]
        neighbor = item - 1
        while neighbor >= 0 and isl[neighbor] > x:
            isl[neighbor + 1] = isl[neighbor]
            neighbor -= 1
        isl[neighbor + 1] = x
    return isl
