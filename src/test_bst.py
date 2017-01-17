"""Test Module for Binary Search Tree."""
from bst import BinarySearchTree


def test_insert_5_is_root():    
    a = BinarySearchTree()
    a.insert(5)
    assert a.root

def test_insert_5_where_root_equals_5():
    a = BinarySearchTree()
    a.insert(5)
    assert a.root.value == 5

def test_insert_5_and_10_and_confirm_right():
    a = BinarySearchTree()
    a.insert(5)
    a.insert(10)
    assert a.root.right.value == 10

def test_insert_many_numbers():
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
