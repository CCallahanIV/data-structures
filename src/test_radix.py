"""Test radix sort."""

from radix import radix_sort
import pytest
import random


@pytest.fixture
def rand_list1():
    """A random sized list of random integers."""
    a = random
    b = random
    c = a.randint(0, 300)
    d = b.sample(range(0, 300), c)
    return d


@pytest.fixture
def rand_list2():
    """A random sized list of random integers."""
    a = random
    b = random
    c = a.randint(0, 300)
    d = b.sample(range(0, 300), c)
    return d


PARAMS_LIST_NO_REPEATS_NO_DECIMALS = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1], [1]),
    ([2, 1], [1, 2]),
]

PARAMS_LIST_REPEATS_NO_DECIMALS = [
    ([1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1]),
    ([55, 44, 44, 55], [44, 44, 55, 55]),
    ([55, 44, 55, 44], [44, 44, 55, 55]),
    ([44, 55, 77, 66, 66], [44, 55, 66, 66, 77]),
]


def test_rand_list1_sorted(rand_list1):
    """Test if the random list is sorted."""
    new_list = rand_list1[:]
    assert radix_sort(rand_list1) == sorted(new_list)


def test_rand_list2_sorted(rand_list2):
    """Test if the random list is sorted."""
    new_list = rand_list2[:]
    assert radix_sort(rand_list2) == sorted(new_list)


@pytest.mark.parametrize('n, result', PARAMS_LIST_NO_REPEATS_NO_DECIMALS)
def test_list_no_repeats_no_decimals(n, result):
    """Test input lists with no repeats and no decimals."""
    assert radix_sort(n) == result


@pytest.mark.parametrize('n, result', PARAMS_LIST_REPEATS_NO_DECIMALS)
def test_list_repeats_no_decimals(n, result):
    """Test input lists with repeats and no decimals."""
    assert radix_sort(n) == result
