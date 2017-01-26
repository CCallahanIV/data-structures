"""This module tests the trie implementation."""

import pytest


@pytest.fixture
def e_trie():
    """Fixture to crate an empty tree."""
    from trie import Trie
    return Trie()


def test_create_emtpy_tree(e_trie):
    """Test creating an empty Trie."""
    from trie import Trie
    assert isinstance(e_trie, Trie)


def test_insert_single_letter_sets_root(e_trie):
    """Test inserting a single letter word sets root."""
    e_trie.insert('a')
    assert e_trie.root.children['a'].end is True
    assert e_trie.root.children['a'].children == {}


def test_insert_word_creates_single_branch(e_trie):
    """Test inserting a single world creates branch as expected."""
    from trie import Node
    e_trie.insert('word')
    assert isinstance(e_trie.root.children['w'], Node)
    assert e_trie.root.children['w'].children['o'].children['r'].children['d'].end is True
    assert e_trie.root.children['w'].prev is e_trie.root


def test_insert_second_word_creates_branch(e_trie):
    """Test inserting second word creates branch off first word."""
    e_trie.insert('word')
    e_trie.insert('worst')
    assert list(e_trie.root.children.keys()) == ['w']
    assert len(e_trie.root.children['w'].children['o'].children['r'].children) == 2
    assert e_trie.root.children['w'].children['o'].children['r'].children['d'].end is True
    assert e_trie.root.children['w'].children['o'].children['r'].children['s'].children['t'].end is True


def test_second_word_no_forks(e_trie):
    """Test inserting a second word with different first letter."""
    e_trie.insert('sword')
    e_trie.insert('word')
    assert len(e_trie.root.children) == 2
    assert e_trie.root.children['w'].prev == e_trie.root
    assert len(e_trie.root.children['s'].children) == 1
    assert len(e_trie.root.children['s'].children['w'].children) == 1
    assert len(e_trie.root.children['s'].children['w'].children['o'].children) == 1
    assert len(e_trie.root.children['s'].children['w'].children['o'].children['r'].children) == 1


def test_insert_short_shared_word(e_trie):
    e_trie.insert('wordless')
    e_trie.insert('word')
    assert len(e_trie.root.children) == 1
    assert e_trie.root.children['w'].children['o'].children['r'].children['d'].end is True
    assert e_trie.root.children['w'].children['o'].children['r'].children['d'].children['l'].children['e'].children['s'].children['s'].end is True


def test_insert_long_shared_word(e_trie):
    e_trie.insert('word')
    e_trie.insert('wordless')
    assert len(e_trie.root.children) == 1
    assert e_trie.root.children['w'].children['o'].children['r'].children['d'].end is True
    assert e_trie.root.children['w'].children['o'].children['r'].children['d'].children['l'].children['e'].children['s'].children['s'].end is True
