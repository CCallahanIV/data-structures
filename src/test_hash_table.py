"""Test module for Hash Table."""

from hash_table import HashTable
import pytest


@pytest.fixture
def colin_ben_filled_hash_table():
    """Fixture for a filled hash table using the words from a dictionary text file hashed with the Colin-Ben hashing algorithm."""
    test_table = HashTable('colin-ben')
    for line in open('/usr/share/dict/words'):
        test_table.set(line, line)
    return test_table


@pytest.fixture
def additive_filled_hash_table():
    """Fixture for a filled hash table using the words from a dictionary text file hashed with the additive technique."""
    test_table = HashTable('additive')
    for line in open('/usr/share/dict/words'):
        test_table.set(line, line)
    return test_table


@pytest.fixture
def colin_ben_filled_hash_table_tiny():
    """Fixture for a filled hash table using the words from a dictionary text file hashed with the Colin-Ben hashing algorithm."""
    test_table = HashTable('colin-ben')
    test_table.set('tornado', 25)
    test_table.set('kangaroo', 50)
    return test_table


def test_table_correct(colin_ben_filled_hash_table):
    """Testing that get works correctly."""
    count = 0
    for line in open('/usr/share/dict/words'):
        count += 1
        if colin_ben_filled_hash_table.get(line) != line:
            assert False
    assert True


def test_table_correct2(additive_filled_hash_table):
    """Testing that get works correctly."""
    # import pdb; pdb.set_trace()
    for line in open('/usr/share/dict/words'):
        if additive_filled_hash_table.get(line) != line:
            assert False
    assert True


def test_table_correct_tiny(colin_ben_filled_hash_table_tiny):
    """Testing that get works correctly."""
    assert colin_ben_filled_hash_table_tiny.get('kangaroo') == 50
    assert colin_ben_filled_hash_table_tiny.get('koala') == 'Key not in hash table.'
