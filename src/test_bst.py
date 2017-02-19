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
    assert e_tree.root.parent is None


def test_insert_second_node_adds_child_correctly(e_tree):
    """Test inserting a second node adds child appropriately."""
    e_tree.insert(10)
    e_tree.insert(15)
    assert e_tree.root.right.value == 15
    assert e_tree.root.left is None
    assert e_tree.root.right.parent is e_tree.root


def test_insert_third_node_adds_child_correctly(e_tree):
    """Test inserting a third node adds child appropriately."""
    e_tree.insert(10)
    e_tree.insert(15)
    e_tree.insert(5)
    assert e_tree.root.left.value == 5
    assert e_tree.root.right.value == 15
    assert e_tree.root.value == 10
    assert e_tree.root.left.parent is e_tree.root


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


def test_traversals_empty_tree(e_tree):
    """Test breadth first traversal on empty and small trees."""
    new = e_tree.breadth_first()
    with pytest.raises(StopIteration):
        next(new)
    new_post = e_tree.post_order()
    with pytest.raises(StopIteration):
        next(new_post)
    new_pre = e_tree.pre_order()
    with pytest.raises(StopIteration):
        next(new_pre)
    new_in = e_tree.in_order()
    with pytest.raises(StopIteration):
        next(new_in)


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


def test_delete_empty_tree(e_tree):
    """Test that deleting a value in an empty tree raises an error."""
    with pytest.raises(IndexError):
        assert e_tree.delete(12)


def test_delete_tree_of_one(e_tree):
    """Test delete from a tree with a single value removes that node."""
    e_tree.insert(12)
    e_tree.delete(12)
    assert e_tree.size() == 0
    assert e_tree.root is None


def test_delete_tree_value_not_present(m_tree):
    """Test that deleting a value not present in tree raises an exception."""
    with pytest.raises(ValueError):
        m_tree.delete(42)


def test_deleting_correctly_moves_nodes(m_tree):
    """Test that deleting root value correctly moves the nodes."""
    expected = [3, 5, 7, 8, 13, 15]
    m_tree.delete(10)
    test_gen = m_tree.in_order()
    for i in range(len(m_tree)):
        assert next(test_gen) == expected[i]
    assert m_tree.contains(10) is False


def test_delete_leaf(m_tree):
    """Test deleting a leaf leaves a correct tree."""
    expected = [5, 7, 8, 10, 13, 15]
    m_tree.delete(3)
    test_gen2 = m_tree.in_order()
    for i in range(len(m_tree)):
        assert next(test_gen2) == expected[i]
    assert m_tree.contains(3) is False


def test_delete_interior_leaf(m_tree):
    """Test deleting an interior leaf."""
    expected = [3, 5, 7, 10, 13, 15]
    m_tree.delete(8)
    test_gen3 = m_tree.in_order()
    for i in range(len(m_tree)):
        assert expected[i] == next(test_gen3)
    assert m_tree.contains(8) is False


def test_delete_node_has_one_child(m_tree):
    """Test deleting node with one child leaves correct tree."""
    expected = [3, 5, 8, 10, 13, 15]
    m_tree.delete(7)
    test_gen4 = m_tree.in_order()
    for i in range(len(m_tree)):
        assert expected[i] == next(test_gen4)
    assert m_tree.root.left.value == 8
    assert m_tree.contains(7) is False
