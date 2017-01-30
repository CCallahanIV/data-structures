"""Test the insertion sort algorithm."""


def test_insertion_sort_list_of_one():
    """Test insertion sort returns list of one item."""
    from insertion_sort import insertion_sort
    assert insertion_sort([1]) == [1]


def test_ins_sort_returns_sorted_list_given_sorted_list():
    """Test insertion sort returns same list given a sorted list."""
    from insertion_sort import insertion_sort
    test_list = [1, 2, 3, 4, 5]
    assert insertion_sort(test_list) == test_list


def test_ins_sort_sorts_small_list():
    """Test insertion sort sorts a small list."""
    from insertion_sort import insertion_sort
    test_list = [3, 5, 6, 2, 8]
    assert insertion_sort(test_list) == sorted(test_list)


def test_insertion_sort_sorts_bigger_list():
    """Test insertion sort on a larger list with repeated values."""
    from insertion_sort import insertion_sort
    test_list = [9, 4, 6, 8, 3, 1, 3, 8, 9]
    assert insertion_sort(test_list) == sorted(test_list)
