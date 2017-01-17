"""Test Module for Binary Search Tree."""
from bst import BinarySearchTree


def test_insert_5_is_root():
    """Test the insert function."""
    a = BinarySearchTree()
    a.insert(5)
    assert a.root


def test_insert_5_where_root_equals_5():
    """Test the insert funciton."""
    a = BinarySearchTree()
    a.insert(5)
    assert a.root.value == 5


def test_insert_5_and_10_and_confirm_right():
    """Test the insert function."""
    a = BinarySearchTree()
    a.insert(5)
    a.insert(10)
    assert a.root.right.value == 10


def test_insert_many_numbers():
    """Test the insert function."""
    a = BinarySearchTree()
    a.insert(8)
    a.insert(10)
    a.insert(3)
    a.insert(14)
    a.insert(13)
    a.insert(1)
    a.insert(6)
    a.insert(7)
    a.insert(4)
    assert a.root.right.right.left.value == 13
    assert a.root.left.value == 3
    assert a.root.right.right.value == 14
    assert a.root.value == 8
    assert a.root.left.right.left.value == 4


def test_size_returns_size_of_binary_search_tree():
    """Test that the size method returns size of the bst."""
    a = BinarySearchTree()
    a.insert(8)
    a.insert(10)
    a.insert(3)
    a.insert(14)
    a.insert(13)
    a.insert(1)
    a.insert(6)
    a.insert(7)
    a.insert(4)
    assert a.size() == 9


def test_binary_search_tree_contains_value():
    """Test that the contains method returns True if value in binary search tree."""
    a = BinarySearchTree()
    a.insert(8)
    a.insert(10)
    a.insert(3)
    a.insert(14)
    a.insert(13)
    a.insert(1)
    a.insert(6)
    a.insert(7)
    a.insert(4)
    assert a.contains(4)


def test_binary_search_tree_does_not_contain_value():
    """Test that the contains method returns True if value in binary search tree."""
    a = BinarySearchTree()
    a.insert(8)
    a.insert(10)
    a.insert(3)
    a.insert(14)
    a.insert(13)
    a.insert(1)
    a.insert(6)
    a.insert(7)
    a.insert(4)
    assert a.contains(100) is False


def test_search_5():
    """Test the search function."""
    a = BinarySearchTree()
    a.insert(5)
    assert a.search(5) == a.root


def test_search_10():
    """Test the search function."""
    a = BinarySearchTree()
    a.insert(5)
    a.insert(10)
    assert a.search(10) == a.root.right


def test_search_empty():
    """Test the search function."""
    a = BinarySearchTree()
    assert a.search(5) is None


def test_search_none():
    """Test the search function."""
    a = BinarySearchTree()
    a.insert(8)
    a.insert(10)
    a.insert(3)
    a.insert(14)
    a.insert(13)
    a.insert(1)
    a.insert(6)
    a.insert(7)
    a.insert(4)
    assert a.search(100) is None


# def test_depth_zero():
#     """Test the depth function."""
#     a = BinarySearchTree()
#     assert a.depth == 0


# def test_depth_one():
#     """Test the depth function."""
#     a = BinarySearchTree()
#     a.insert(8)
#     assert a.depth == 1


# def test_depth_many():
#     """Test the depth function."""
#     a = BinarySearchTree()
#     a.insert(8)
#     a.insert(10)
#     a.insert(3)
#     a.insert(14)
#     a.insert(13)
#     a.insert(1)
#     a.insert(6)
#     a.insert(7)
#     a.insert(4)
#     assert a.depth == 4


# def test_balance():
#     """Test the balance function."""
#     a = BinarySearchTree()
#     a.insert(8)
#     a.insert(10)
#     a.insert(3)
#     a.insert(14)
#     a.insert(13)
#     a.insert(1)
#     a.insert(6)
#     a.insert(7)
#     assert a.balance == -1
