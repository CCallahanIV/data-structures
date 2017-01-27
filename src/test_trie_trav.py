from trie_trav import Trie
import pytest

SIMPLE_INPUT = ['abort', 'tony', 'borg', 'russia']
MODERATE_INPUT = ['fast', 'faster', 'fastest', 'fastener', 'breakfasttime']
COMPLEX_INPUT = ['aaaaaa', 'aardvark', 'aaraal', 'aapppp', 'aapear', 'tornado', 'ado', 'tor', 'to', 'o', 'oo', 'oooo', 'elephant', 'elevate', 'elephants']

PARAMS_SIMPLE = [
    ('rus', ['s', 'i', 'a']),
    ('o', ['r', 't', 'n', 'y', 'r', 'g']),
    ('a', ['b', 'o', 'r', 't']),
    ('r', ['t', 'g'])
]

PARAMS_MODERATE = [
    ('fast', ['e', 'r', 's', 't', 'n', 'e', 'r', 't', 'i', 'm', 'e']),
    ('f', ['a', 's', 't', 'e', 'r', 's', 't', 'n', 'e', 'r', 'a', 's', 't', 't', 'i', 'm', 'e']),
    ('a', ['s', 't', 'e', 'r', 's', 't', 'n', 'e', 'r', 'k', 'f', 'a', 's', 't', 'i', 'm', 'e']),
    ('faste', ['r', 's', 't', 'n', 'e', 'r']),
    ('t', ['r', 'r', 's', 't', 'n', 'e', 'r', 't', 'i', 'm', 'e']),
    ('faster', []),
]

PARAMS_COMPLEX = [
    ('a', ['d', 'o', 'a', 'a', 'a', 'a', 'a', 'r', 'd', 'v', 'a', 'r', 'k', 'a', 'a', 'l', 'p', 'p', 'p', 'p', 'e', 'a', 'r', 'd', 'o', 'n', 't', 's', 't', 'e']),
    ('', []),
    ('', []),
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


@pytest.mark.parametrize('n, result', PARAMS_SIMPLE)
def test_traversal_simple(simple_trie, n, result):
    """Test traversal with input 'o'."""
    g = simple_trie.traversal(n)
    assert list(g) == result


@pytest.mark.parametrize('n, result', PARAMS_MODERATE)
def test_traversal_moderate(simple_trie, n, result):
    """Test traversal with input 'o'."""
    g = simple_trie.traversal(n)
    assert list(g) == result


@pytest.mark.parametrize('n, result', PARAMS_COMPLEX)
def test_traversal_complex(simple_trie, n, result):
    """Test traversal with input 'o'."""
    g = simple_trie.traversal(n)
    assert list(g) == result
