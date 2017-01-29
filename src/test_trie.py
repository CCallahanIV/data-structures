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
    ('t', False)
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
