"""Test insertion sort."""

from insertion_sort import insertion_sort
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
    ([-1, 8], [-1, 8]),
]

PARAMS_LIST_REPEATS_NO_DECIMALS = [
    ([1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1]),
    ([0, -0], [0, 0]),
    ([55, 44, 44, 55], [44, 44, 55, 55]),
    ([55, 44, 55, 44], [44, 44, 55, 55]),
    ([44, 55, 77, 66, 66], [44, 55, 66, 66, 77]),
    ([55, 55, -44, 66, 77], [-44, 55, 55, 66, 77]),
]

PARAMS_LIST_DECIMALS_NO_REPEATS = [
    ([1.0, 1, 3.5], [1, 1.0, 3.5]),
    ([3.14, 2.67], [2.67, 3.14]),
    ([2.67, 3.14], [2.67, 3.14]),
    ([345543.234534522646654356345643563, 34.53453452456266], [34.53453452456266, 345543.234534522646654356345643563]),
    ([0.2452345234, .11111111111], [.11111111111, 0.2452345234]),
]

PARAMS_LIST_DECIMALS_AND_REPEATS = [
    ([1.5, 1, 1, 1.5, 1, 1.5, 1, 0], [0, 1, 1, 1, 1, 1.5, 1.5, 1.5]),
    ([-20, 0, -22.2], [-22.2, -20, 0]),
    ([-3, -3.555556, -3.555555], [-3.555556, -3.555555, -3]),
    ([.0980248972834], [.0980248972834]),
    ([978120346.19238471934, -9782947.98797052], [-9782947.98797052, 978120346.19238471934]),
    ([1.1111111111111, .555555555555, -.43434343434343, -.343434343434343434343434], [-.43434343434343, -.343434343434343434343434, .555555555555, 1.1111111111111]),
]

WORD_PARAMS_LIST = [
    (["the", "brown", "cow", "doth", "protest", "too", "much"], ["brown", "cow", "doth", "much", "protest", "the", "too"]),
    (["sometimes", "Brown", "altoids", "look", "so", "very", "strange", "in", "town", "now"], ["Brown", "altoids", "in", "look", "now", "so", "sometimes", "strange", "town", "very"]),
    (["Big", "SMALL", "BOY", "almost", "ZOO", "SiNg"], ["BOY", "Big", "SMALL", "SiNg", "ZOO", "almost"])
]


def test_rand_list1_sorted(rand_list1):
    """Test if the random list is sorted."""
    new_list = rand_list1[:]
    assert insertion_sort(rand_list1) == sorted(new_list)


def test_rand_list2_sorted(rand_list2):
    """Test if the random list is sorted."""
    new_list = rand_list2[:]
    assert insertion_sort(rand_list2) == sorted(new_list)


@pytest.mark.parametrize('n, result', PARAMS_LIST_NO_REPEATS_NO_DECIMALS)
def test_list_no_repeats_no_decimals(n, result):
    """Test input lists with no repeats and no decimals."""
    assert insertion_sort(n) == result


@pytest.mark.parametrize('n, result', PARAMS_LIST_REPEATS_NO_DECIMALS)
def test_list_repeats_no_decimals(n, result):
    """Test input lists with repeats and no decimals."""
    assert insertion_sort(n) == result


@pytest.mark.parametrize('n, result', PARAMS_LIST_DECIMALS_NO_REPEATS)
def test_list_decimals_no_repeats(n, result):
    """Test input lists with decimals and no repeats."""
    assert insertion_sort(n) == result


@pytest.mark.parametrize('n, result', PARAMS_LIST_DECIMALS_AND_REPEATS)
def test_list_decimals_and_repeats(n, result):
    """Test input lists with decimals and no repeats."""
    assert insertion_sort(n) == result


@pytest.mark.parametrize('n, result', WORD_PARAMS_LIST)
def test_word_list_with_sorted(n, result):
    """Test list of words with the insertion sort."""
    assert insertion_sort(n) == result
