"""This module tests a binary search tree."""

import pytest


MEDIUM_TREE = [10, 15, 13, 7, 5, 8, 3]


@pytest.fixture
def e_tree():
    """Initialize an empty search tree."""
    from bst import BinarySearchTree
    return BinarySearchTree()


@pytest.fixture
def m_tree():
    """Initialize a search tree of medium complexity."""
    from bst import BinarySearchTree
    b = BinarySearchTree()
    for val in MEDIUM_TREE:
        b.insert(val)
    return b


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


def test_depth_medium_tree(m_tree):
    """Test balance of a medium sized tree."""
    assert m_tree.depth() == 4
    m_tree.insert(1)
    assert m_tree.depth() == 5
    m_tree.insert(17)
    assert m_tree.depth() == 5


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


def test_find_neg_balance_unbalanced_three_node(e_tree):
    """Test finding balance of an unbalanced three node tree."""
    e_tree.insert(20)
    e_tree.insert(15)
    e_tree.insert(10)
    assert e_tree.balance() == -2


def test_find_balance_med_tree(m_tree):
    """Test finding the balance of a medium tree."""
    assert m_tree.balance() == -1
    m_tree.insert(1)
    assert m_tree.balance() == -2
    m_tree.insert(12)
    assert m_tree.balance() == -1


def test_search_medium_tree_returns_true(m_tree):
    """Test searching medium tree returns node."""
    root_result = m_tree.search(10)
    assert root_result.value == 10
    left_result = m_tree.search(3)
    assert left_result.value == 3
    right_result = m_tree.search(13)
    assert right_result.value == 13


def test_search_medium_tree_returns_false(m_tree):
    """Test searching medium tree returns None."""
    assert m_tree.search(20) is None
    assert m_tree.search(0) is None


def test_contains_returns_true(m_tree):
    """Test contains returns true for medium tree."""
    assert m_tree.contains(10) is True
    assert m_tree.contains(3) is True
    assert m_tree.contains(15) is True
    m_tree.insert(1)
    assert m_tree.contains(1) is True


def test_contains_returns_false(m_tree):
    """Test contains returns false for medoum tree."""
    assert m_tree.contains(27) is False


def test_breadth_first_m_tree(m_tree):
    """Test the breadth_first method returns a generator of values in correct order."""
    expected = [10, 7, 15, 5, 8, 13, 3]
    gen_test = m_tree.breadth_first()
    for i in range(len(m_tree)):
        assert next(gen_test) == expected[i]


def test_in_order_m_tree(m_tree):
    """Test the breadth_first method returns a generator of values in correct order."""
    expected = [3, 5, 7, 8, 10, 13, 15]
    gen_test = m_tree.in_order()
    for i in range(len(m_tree)):
        assert next(gen_test) == expected[i]


def test_pre_order_m_tree(m_tree):
    """Test the breadth_first method returns a generator of values in correct order."""
    expected = [10, 7, 5, 3, 8, 15, 13]
    gen_test = m_tree.pre_order()
    for i in range(len(m_tree)):
        test_this = next(gen_test)
        assert test_this == expected[i]


def test_post_order_m_tree(m_tree):
    """Test the breadth_first method returns a generator of values in correct order."""
    expected = [3, 5, 8, 7, 13, 15, 10]
    gen_test = m_tree.post_order()
    for i in range(len(m_tree)):
        assert next(gen_test) == expected[i]
