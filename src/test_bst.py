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


def test_find_total_depth_empty(e_tree):
    """Test finding depth from empty tree."""
    # import pdb; pdb.set_trace()
    assert e_tree.depth() == 0


def test_find_depth_one_node(e_tree):
    """Test finding depth from a one node tree."""
    e_tree.insert(10)
    assert e_tree.depth() == 1


def test_find_depth_two_node(e_tree):
    """Test finding depth from a two node tree."""
    e_tree.insert(10)
    e_tree.insert(15)
    assert e_tree.depth() == 2


def test_find_depth_balanced_three_node(e_tree):
    """Test finding depth from a balanced three node tree."""
    e_tree.insert(10)
    e_tree.insert(15)
    e_tree.insert(5)
    assert e_tree.depth() == 2


def test_find_depth_unbalanced_three_node(e_tree):
    """Test finding depth from an unbalanced three node tree."""
    e_tree.insert(10)
    e_tree.insert(15)
    e_tree.insert(20)
    assert e_tree.depth() == 3


def test_balance_empty(e_tree):
    """Test balance of empty tree."""
    assert e_tree.balance() == 0


def test_balance_one_node(e_tree):
    """Test balance of one node tree."""
    e_tree.insert(10)
    assert e_tree.balance() == 0


def test_balance_two_node(e_tree):
    """Test finding blance from a two node tree."""
    e_tree.insert(10)
    e_tree.insert(15)
    assert e_tree.balance() == 1


def test_find_balance_balanced_three_node(e_tree):
    """Test finding balance from a balanced three node tree."""
    e_tree.insert(10)
    e_tree.insert(15)
    e_tree.insert(5)
    assert e_tree.balance() == 0


def test_find_balance_unbalanced_three_node(e_tree):
    """Test finding balance from an unbalanced three node tree."""
    e_tree.insert(10)
    e_tree.insert(15)
    e_tree.insert(20)
    assert e_tree.balance() == 2
