"""Test Module for Binary Search Tree."""
from bst import BinarySearchTree
import pytest

BST_SIMPLE = [8, 10, 3, 14, 13, 1, 6, 7, 4]
BST_STRAIGHT_LINE = [1, 2, 3, 4, 5, 6, 7]
BST_BIG = [
    30, 50, 45, 60, 15, 25, 10, 47, 42,
    40, 27, 55, 44, 46, 49, 7, 12, 65, 70, 57,
    63, 52, 23, 4, 9, 11, 13, 21, 24, 26, 28
]


@pytest.fixture
def big_bst():
    """Fixture to fill big bst."""
    from bst import BinarySearchTree
    new_tree = BinarySearchTree(BST_BIG)
    return new_tree


@pytest.fixture
def straight_bst():
    """Fixture to fill bst tree with a straight line of nodes down right side."""
    from bst import BinarySearchTree
    new_tree = BinarySearchTree(BST_STRAIGHT_LINE)
    return new_tree


@pytest.fixture
def filled_bst():
    """Fixture to fill the bst tree with nodes."""
    from bst import BinarySearchTree
    new_tree = BinarySearchTree(BST_SIMPLE)
    return new_tree


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


def test_depth_zero():
    """Test the depth function."""
    a = BinarySearchTree()
    assert a.depth() == 0


def test_depth_one():
    """Test the depth function."""
    a = BinarySearchTree()
    a.insert(8)
    assert a.depth() == 1


def test_depth_many():
    """Test the depth function."""
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
    assert a.depth() == 4


def test_balance():
    """Test the balance function."""
    a = BinarySearchTree()
    a.insert(8)
    a.insert(10)
    a.insert(3)
    a.insert(14)
    a.insert(13)
    a.insert(1)
    a.insert(6)
    a.insert(7)
    assert a.balance() == 0


def test_balance_unbalanced_right(filled_bst):
    """Test the balance function."""
    filled_bst.insert(11)
    filled_bst.insert(12)
    assert filled_bst.balance() == 2


def test_balance_unbalanced_left(filled_bst):
    """Test the balance function."""
    filled_bst.insert(5)
    filled_bst.insert(4.5)
    assert filled_bst.balance() == -2


def test_in_order_traversal_first_node_traversed_is_1(filled_bst):
    """In-order traversal will start with 1."""
    in_order_list = []
    for x in filled_bst._in_order_trav():
        in_order_list.append(x)
    assert in_order_list[0] == 1


def test_in_order_traversal_first_node_traversed_is_1_reg(filled_bst):
    """In-order traversal's first value from generator will get a 1."""
    assert filled_bst.in_order() == 1
    assert filled_bst.in_order() == 3
    assert filled_bst.in_order() == 4
    assert filled_bst.in_order() == 6
    assert filled_bst.in_order() == 7
    assert filled_bst.in_order() == 8
    assert filled_bst.in_order() == 10
    assert filled_bst.in_order() == 13
    assert filled_bst.in_order() == 14


def test_pre_order_traversal_first_node_traversed_is_8(filled_bst):
    """Pre-order traversal will get 8."""
    assert filled_bst.pre_order() == 8
    assert filled_bst.pre_order() == 3
    assert filled_bst.pre_order() == 1
    assert filled_bst.pre_order() == 6
    assert filled_bst.pre_order() == 4
    assert filled_bst.pre_order() == 7
    assert filled_bst.pre_order() == 10
    assert filled_bst.pre_order() == 14
    assert filled_bst.pre_order() == 13


def test_post_order_traversal(filled_bst):
    """Post-order traversal."""
    assert filled_bst.post_order() == 1
    assert filled_bst.post_order() == 4
    assert filled_bst.post_order() == 7
    assert filled_bst.post_order() == 6
    assert filled_bst.post_order() == 3
    assert filled_bst.post_order() == 13
    assert filled_bst.post_order() == 14
    assert filled_bst.post_order() == 10
    assert filled_bst.post_order() == 8


def test_delete_empty():
    """Test delete function with empty binary search tree."""
    a = BinarySearchTree()
    assert a.delete(5) is None


def test_delete_filled_root(filled_bst):
    """Test delete of root."""
    a = filled_bst
    assert a.size() == 9
    a.delete(8)
    assert a.size() == 8
    assert a.in_order() == 1
    assert a.in_order() == 3
    assert a.in_order() == 4
    assert a.in_order() == 6
    assert a.in_order() == 7
    assert a.in_order() == 10
    assert a.in_order() == 13
    assert a.in_order() == 14


def test_delete_end(filled_bst):
    """Test delete of root."""
    a = filled_bst
    assert a.size() == 9
    a.delete(1)
    assert a.size() == 8
    assert a.in_order() == 3
    assert a.in_order() == 4
    assert a.in_order() == 6
    assert a.in_order() == 7
    assert a.in_order() == 8
    assert a.in_order() == 10
    assert a.in_order() == 13
    assert a.in_order() == 14


def test_delete_vertex_of_left_sub_head_in_bst(filled_bst):
    """Test delete of a BST's left sub tree's head."""
    a = filled_bst
    a.delete(3)
    assert a.root.value == 8
    assert a.root.left.value == 4
    assert a.root.left.right.value == 6
    assert a.root.left.right.right.value == 7


def test_delete_vertex_of_lower_vertex_with_2_children(filled_bst):
    """Test lower vertex removal at bottom of tree with 2 children."""
    a = filled_bst
    a.delete(6)
    assert a.root.value == 8
    assert a.root.left.right.value == 7
    assert a.root.left.right.left.value == 4
    assert a.root.left.value == 3
    assert a.root.left.left.value == 1
    assert a.root.right.value == 10


def test_delete(straight_bst):
    """Test removal of node from straight line bst."""
    a = straight_bst
    a.delete(4)
    assert a.root.value == 1
    assert a.root.right.value == 2
    assert a.root.right.right.value == 3
    assert a.root.right.right.right.value == 5
    assert a.root.right.right.right.right.value == 6


def test_node_deletion_from_big_tree_with_grand_children(big_bst):
    """Test deletion of node in big bst tree with children and grand children."""
    a = big_bst
    a.delete(45)
    assert a.root.right.left.value == 46
    assert a.root.right.left.right.value == 47
    assert a.root.right.left.left.value == 42
    assert a.root.right.left.right.right.value == 49
    assert a.root.right.left.right.left is None


def test_deletion_from_big_tree_with_great_grand_children(big_bst):
    """Test deletion of node in big bst tree with children and grand children."""
    a = big_bst
    a.delete(50)
    assert a.root.right.value == 52
    assert a.root.right.left.value == 45
    assert a.root.right.right.value == 60
    assert a.root.right.right.left.value == 55
    assert a.root.right.right.right.value == 65
    assert a.root.right.right.left.right.value == 57
    assert a.root.right.right.left.left is None
    assert a.root.right.right.right.right.value == 70
    assert a.root.right.right.right.left.value == 63


def test_node_deletion_from_big_tree_root(big_bst):
    """Test root deletion on big_bst."""
    a = big_bst
    a.delete(30)
    assert a.root.value == 40
    assert a.root.right.value == 50
    assert a.root.right.left.value == 45
    assert a.root.right.left.left.value == 42
    assert a.root.right.left.left.left is None
    assert a.root.right.left.left.right.value == 44
    assert a.root.right.right.value == 60
    assert a.root.right.right.left.value == 55
    assert a.root.right.right.right.value == 65
    assert a.root.right.right.left.right.value == 57
    assert a.root.right.right.left.left.value == 52
    assert a.root.right.right.right.right.value == 70
    assert a.root.right.right.right.left.value == 63


def test_node_deletion_from_big_tree_furthest_left(big_bst):
    """Test furthest left node deletion on big_bst."""
    a = big_bst
    a.delete(4)
    assert a.root.value == 30
    assert a.root.left.value == 15
    assert a.root.left.left.value == 10
    assert a.root.left.left.left.value == 7
    assert a.root.left.left.left.left is None
    assert a.root.right.value == 50
    assert a.root.right.left.value == 45
    assert a.root.right.left.left.value == 42
    assert a.root.right.left.left.left.value == 40
    assert a.root.right.left.left.right.value == 44
    assert a.root.right.right.value == 60
    assert a.root.right.right.left.value == 55
    assert a.root.right.right.right.value == 65
    assert a.root.right.right.left.right.value == 57
    assert a.root.right.right.left.left.value == 52
    assert a.root.right.right.right.right.value == 70
    assert a.root.right.right.right.left.value == 63


def test_big_bst(big_bst):
    """Test nodes in proper places in big_bst."""
    a = big_bst
    assert a.root.value == 30
    assert a.root.left.value == 15
    assert a.root.left.right.value == 25
    assert a.root.left.right.left.value == 23
    assert a.root.left.left.value == 10
    assert a.root.left.left.right.value == 12
    assert a.root.left.left.right.right.value == 13
    assert a.root.left.left.right.left.value == 11
    assert a.root.left.left.left.value == 7
    assert a.root.left.left.left.right.value == 9
    assert a.root.left.left.left.left.value == 4
    assert a.root.right.value == 50
    assert a.root.right.left.value == 45
    assert a.root.right.left.left.value == 42
    assert a.root.right.left.left.left.value == 40
    assert a.root.right.left.left.right.value == 44
    assert a.root.right.right.value == 60
    assert a.root.right.right.left.value == 55
    assert a.root.right.right.right.value == 65
    assert a.root.right.right.left.right.value == 57
    assert a.root.right.right.left.left.value == 52
    assert a.root.right.right.right.right.value == 70
    assert a.root.right.right.right.left.value == 63


def test_big_bst_insert_delete_min_node_with_right_child(big_bst):
    """Test deletion of node with min node with right child."""
    a = big_bst
    a.insert(22)
    a.delete(15)
    assert a.root.value == 30
    assert a.root.left.value == 21
    assert a.root.left.right.value == 25
    assert a.root.left.right.left.value == 23
    assert a.root.left.right.left.left.value == 22
    assert a.root.left.left.value == 10
    assert a.root.left.left.right.value == 12
    assert a.root.left.left.right.right.value == 13
    assert a.root.left.left.right.left.value == 11
    assert a.root.left.left.left.value == 7
    assert a.root.left.left.left.right.value == 9
    assert a.root.left.left.left.left.value == 4
    assert a.root.right.value == 50
    assert a.root.right.left.value == 45
    assert a.root.right.left.left.value == 42
    assert a.root.right.left.left.left.value == 40
    assert a.root.right.left.left.right.value == 44
    assert a.root.right.right.value == 60
    assert a.root.right.right.left.value == 55
    assert a.root.right.right.right.value == 65
    assert a.root.right.right.left.right.value == 57
    assert a.root.right.right.left.left.value == 52
    assert a.root.right.right.right.right.value == 70
    assert a.root.right.right.right.left.value == 63


def test_big_bst_insert_delete_root_min_node_with_right_child(big_bst):
    """Test deletion of root node with min node with right child."""
    a = big_bst
    a.insert(41)
    a.delete(30)
    a = big_bst
    assert a.root.value == 40
    assert a.root.left.value == 15
    assert a.root.left.right.value == 25
    assert a.root.left.right.left.value == 23
    assert a.root.left.left.value == 10
    assert a.root.left.left.right.value == 12
    assert a.root.left.left.right.right.value == 13
    assert a.root.left.left.right.left.value == 11
    assert a.root.left.left.left.value == 7
    assert a.root.left.left.left.right.value == 9
    assert a.root.left.left.left.left.value == 4
    assert a.root.right.value == 50
    assert a.root.right.left.value == 45
    assert a.root.right.left.left.value == 42
    assert a.root.right.left.left.left.value == 41
    assert a.root.right.left.left.right.value == 44
    assert a.root.right.right.value == 60
    assert a.root.right.right.left.value == 55
    assert a.root.right.right.right.value == 65
    assert a.root.right.right.left.right.value == 57
    assert a.root.right.right.left.left.value == 52
    assert a.root.right.right.right.right.value == 70
    assert a.root.right.right.right.left.value == 63


def test_multiple_delete_to_empty(filled_bst):
    """Test that all nodes can be deleted and size output reflects this."""
    a = filled_bst
    a.delete(8)
    a.delete(10)
    a.delete(3)
    a.delete(14)
    a.delete(13)
    a.delete(1)
    a.delete(6)
    a.delete(7)
    a.delete(4)
    assert a.size() == 0
