"""Test module for Trie Tree."""

from trie import Trie
import pytest


SIMPLE_INPUT = ['abort', 'tony', 'borg', 'russia']
MODERATE_INPUT = ['fast', 'faster', 'fastest', 'fastener', 'breakfasttime']
COMPLEX_INPUT = ['aaaaaa', 'aardvark', 'aaraal', 'aapppp', 'aapear', 'tornado', 'ado', 'tor', 'to', 'o', 'oo', 'oooo', 'elephant', 'elevate', 'elephants']

PARAMS_CONTAINS_SIMPLE = [
    ('abort', True),
    ('tony', True),
    ('ab', False),
    ('z', False),
    ('a', False),
    ('t', False),
]


@pytest.fixture
def simple_trie():
    """Trie with simple input."""
    a = Trie()
    for each in SIMPLE_INPUT:
        a.insert(each)
    return a


@pytest.fixture
def moderate_trie():
    """Trie with moderate input."""
    a = Trie()
    for each in MODERATE_INPUT:
        a.insert(each)
    return a


@pytest.fixture
def complex_trie():
    """Trie with complex input."""
    a = Trie()
    for each in COMPLEX_INPUT:
        a.insert(each)
    return a


@pytest.mark.parametrize('n, result', PARAMS_CONTAINS_SIMPLE)
def test_contains_simple(simple_trie, n, result):
    """Test contains function."""
    assert simple_trie.contains(n) == result


def test_size_of_an_empty_trie():
    """Test for the size of an empty trie."""
    a = Trie()
    assert a.size() == 0


def test_size_of_a_filled_trie():
    """Test for the size of a filled trie."""
    a = Trie()
    for each in MODERATE_INPUT:
        a.insert(each)
    assert a.size() == 5


def test_removal_from_a_filled_trie():
    """Test the removal of a node from of a filled trie."""
    a = Trie()
    for each in MODERATE_INPUT:
        a.insert(each)
    a.remove("fast")
    assert a.contains("fast") is False


def test_removeal_of_an_empty_trie():
    """Test the removal of a node from an empty trie."""
    a = Trie()
    with pytest.raises(IndexError):
        a.remove("fast")


def test_removal_of_substring_word_of_another_word_in_trie():
    """Test the removal of 'o', where 'oo' and 'oooo' exist too in the trie."""
    a = Trie()
    for each in COMPLEX_INPUT:
        a.insert(each)
    a.remove('o')
    assert a.size() == 14
    assert a.contains('o') is False
