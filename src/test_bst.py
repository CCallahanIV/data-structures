"""This module tests a binary search tree."""

import pytest


@pytest.fixture
def e_tree():
    """Initialize an empty search tree."""
    from bst import BinarySearchTree
    return BinarySearchTree()


def test_init_empty_bst(e_tree):
    """Test initializing an empty tree."""
    from bst import BinarySearchTree
    assert isinstance(e_tree, BinarySearchTree)


def test_insert_first_node_sets_root(e_tree):
    """Test inserting first node sets root."""
    e_tree.insert(1)
    assert e_tree.root.value == 1


def test_insert_second_node_adds_child_correctly(e_tree):
    """Test inserting a second node adds child appropriately."""
    e_tree.insert(10)
    e_tree.insert(15)
    assert e_tree.root.right.value == 15
    assert e_tree.root.left is None


def test_insert_third_node_adds_child_correctly(e_tree):
    """Test inserting a third node adds child appropriately."""
    e_tree.insert(10)
    e_tree.insert(15)
    e_tree.insert(5)
    assert e_tree.root.left.value == 5
    assert e_tree.root.right.value == 15
    assert e_tree.root.value == 10

