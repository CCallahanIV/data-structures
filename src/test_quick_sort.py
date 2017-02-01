"""Test the quick sort algorithm."""

from random import randint


def test_quick_sort_empty_list():
    """Test quick sort on empty list."""
    from quick_sort import quick_sort
    assert quick_sort([]) == []


def test_quick_sort_list_of_one():
    """Test insertion sort returns list of one item."""
    from quick_sort import quick_sort
    assert quick_sort([1]) == [1]


def test_quick_sort_returns_sorted_list_given_sorted_list():
    """Test insertion sort returns same list given a sorted list."""
    from quick_sort import quick_sort
    test_list = [1, 2, 3, 4, 5]
    assert quick_sort(test_list) == test_list


def test_quick_sort_sorts_small_list():
    """Test insertion sort sorts a small list."""
    from quick_sort import quick_sort
    test_list = [3, 5, 6, 2, 8]
    assert quick_sort(test_list) == sorted(test_list)


def test_quick_sort_sorts_bigger_list():
    """Test insertion sort on a larger list with repeated values."""
    from quick_sort import quick_sort
    test_list = [9, 4, 6, 8, 3, 1, 3, 8, 9]
    assert quick_sort(test_list) == sorted(test_list)


def test_quick_sort_on_randomized_list():
    """Test insertion sort with random list of random length."""
    from quick_sort import quick_sort
    test_list = [randint(0, 100) for i in range(randint(10, 100))]
    assert quick_sort(test_list) == sorted(test_list)
