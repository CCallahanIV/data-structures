"""Test Module for Balanced Binary Search Tree."""
from balanced_bst import BinarySearchTree
import pytest

BST_ROT_2_R_1 = [3, 2]
BST_ROT_2_L_3 = [1, 2]
BST_ROT_LR_GC_7 = [10, 12, 5, 8, 2]
BST_ROT_RL = [10, 5, 15, 13, 20]


@pytest.fixture
def filled_bst_rot_2_r_1():
    """Fixture for a 2 node tree for a right rotation with insertion of 1."""
    new_tree = BinarySearchTree(BST_ROT_2_R_1)
    return new_tree


@pytest.fixture
def filled_bst_rot_2_l_3():
    """Fixture for a 2 node tree for a left rotation with insertion of 3."""
    new_tree = BinarySearchTree(BST_ROT_2_L_3)
    return new_tree


@pytest.fixture
def filled_bst_rot_lr_gc_7():
    """Fixture for a binary search tree for a left-right rotation with insertion of 7 to tree 10, 12, 5, 8, 2."""
    new_tree = BinarySearchTree(BST_ROT_LR_GC_7)
    return new_tree


@pytest.fixture
def filled_bst_rot_rl():
    """Fixture for a binary search tree for a right-left rotation."""
    new_tree = BinarySearchTree(BST_ROT_RL)
    return new_tree


def test_simple_3_node_right_rotation(filled_bst_rot_2_r_1):
    """Balance bst via right rotation, when adding 1 to tree of 3, 2."""
    a = filled_bst_rot_2_r_1
    a.insert(1)
    assert a.root.value == 2
    assert a.root.right.value == 3
    assert a.root.left.value == 1


def test_simple_3_node_left_rotation(filled_bst_rot_2_l_3):
    """Balance bst via left rotation, when adding 3 to tree of 1, 2."""
    a = filled_bst_rot_2_l_3
    a.insert(3)
    assert a.root.value == 2
    assert a.root.right.value == 3
    assert a.root.left.value == 1


def test_left_right_rotation(filled_bst_rot_lr_gc_7):
    """Balance bst via left-right rotation, when adding 7 to tree of 10, 12, 5, 8, 2."""
    a = filled_bst_rot_lr_gc_7
    a.insert(7)
    assert a.root.value == 8
    assert a.root.right.value == 10
    assert a.root.left.value == 5
    assert a.root.left.right.value == 7
    assert a.root.left.left.value == 2
    assert a.root.right.right.value == 12


def test_bst_empty_tree():
    """Test balancing empty tree."""
    a = BinarySearchTree()
    assert a.root is None


def test_bst_1_value():
    """Test balancing tree with one value."""
    a = BinarySearchTree()
    a.insert(1)
    assert a.root.value == 1
    assert a.root.right is None
    assert a.root.left is None


def test_bst_2_values():
    """Test balancing tree with two values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    assert a.root.value == 1
    assert a.root.right.value == 2
    assert a.root.left is None


def test_bst_3_values():
    """Test balancing tree with three values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    assert a.root.value == 2
    assert a.root.right.value == 3
    assert a.root.left.value == 1


def test_bst_4_values():
    """Test balancing tree with four values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    assert a.root.value == 2
    assert a.root.right.value == 3
    assert a.root.left.value == 1
    assert a.root.right.right.value == 4


def test_bst_5_values():
    """Test balancing tree with five values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    assert a.root.value == 2
    assert a.root.right.value == 4
    assert a.root.left.value == 1
    assert a.root.right.right.value == 5
    assert a.root.right.left.value == 3


def test_bst_6_values():
    """Test balancing tree with six values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    assert a.root.value == 4
    assert a.root.right.value == 5
    assert a.root.left.value == 2
    assert a.root.right.right.value == 6
    assert a.root.left.left.value == 1
    assert a.root.left.right.value == 3


def test_bst_7_values():
    """Test balancing tree with seven values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    assert a.root.value == 4
    assert a.root.right.value == 6
    assert a.root.left.value == 2
    assert a.root.right.right.value == 7
    assert a.root.left.left.value == 1
    assert a.root.left.right.value == 3
    assert a.root.right.left.value == 5


def test_bst_8_values():
    """Test balancing tree with eight values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    assert a.root.value == 4
    assert a.root.right.value == 6
    assert a.root.left.value == 2
    assert a.root.right.right.value == 7
    assert a.root.left.left.value == 1
    assert a.root.left.right.value == 3
    assert a.root.right.left.value == 5
    assert a.root.right.right.right.value == 8


def test_bst_9_values():
    """Test balancing tree with nine values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    a.insert(9)
    assert a.root.value == 4
    assert a.root.right.value == 6
    assert a.root.left.value == 2
    assert a.root.right.right.value == 8
    assert a.root.left.left.value == 1
    assert a.root.left.right.value == 3
    assert a.root.right.left.value == 5
    assert a.root.right.right.right.value == 9
    assert a.root.right.right.left.value == 7


def test_bst_10_values():
    """Test balancing tree with ten values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    a.insert(9)
    a.insert(10)
    assert a.root.value == 4
    assert a.root.right.value == 8
    assert a.root.left.value == 2
    assert a.root.right.right.value == 9
    assert a.root.left.left.value == 1
    assert a.root.left.right.value == 3
    assert a.root.right.right.right.value == 10
    assert a.root.right.left.value == 6
    assert a.root.right.left.right.value == 7
    assert a.root.right.left.left.value == 5


def test_bst_11_values():
    """Test balancing tree with eleven values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    a.insert(9)
    a.insert(10)
    a.insert(11)
    assert a.root.value == 4
    assert a.root.right.value == 8
    assert a.root.left.value == 2
    assert a.root.right.right.value == 10
    assert a.root.left.left.value == 1
    assert a.root.left.right.value == 3
    assert a.root.right.right.right.value == 11
    assert a.root.right.right.left.value == 9
    assert a.root.right.left.value == 6
    assert a.root.right.left.right.value == 7
    assert a.root.right.left.left.value == 5


def test_bst_12_values():
    """Test balancing tree with twelve values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    a.insert(9)
    a.insert(10)
    a.insert(11)
    a.insert(12)
    assert a.root.value == 8
    assert a.root.right.value == 10
    assert a.root.right.right.value == 11
    assert a.root.right.left.value == 9
    assert a.root.right.right.right.value == 12
    assert a.root.left.value == 4
    assert a.root.left.left.value == 2
    assert a.root.left.left.left.value == 1
    assert a.root.left.left.right.value == 3
    assert a.root.left.right.value == 6
    assert a.root.left.right.left.value == 5
    assert a.root.left.right.right.value == 7


def test_bst_13_values():
    """Test balancing tree with thirteen values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    a.insert(9)
    a.insert(10)
    a.insert(11)
    a.insert(12)
    a.insert(13)
    assert a.root.value == 8
    assert a.root.right.value == 10
    assert a.root.right.right.value == 12
    assert a.root.right.left.value == 9
    assert a.root.right.right.right.value == 13
    assert a.root.right.right.left.value == 11
    assert a.root.left.value == 4
    assert a.root.left.left.value == 2
    assert a.root.left.left.left.value == 1
    assert a.root.left.left.right.value == 3
    assert a.root.left.right.value == 6
    assert a.root.left.right.left.value == 5
    assert a.root.left.right.right.value == 7


def test_bst_14_values():
    """Test balancing tree with fourteen values."""
    a = BinarySearchTree()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(8)
    a.insert(9)
    a.insert(10)
    a.insert(11)
    a.insert(12)
    a.insert(13)
    a.insert(14)
    assert a.root.value == 8
    assert a.root.right.value == 12
    assert a.root.right.right.value == 13
    assert a.root.right.left.value == 10
    assert a.root.right.right.right.value == 14
    assert a.root.right.left.left.value == 9
    assert a.root.right.left.right.value == 11
    assert a.root.left.value == 4
    assert a.root.left.left.value == 2
    assert a.root.left.left.left.value == 1
    assert a.root.left.left.right.value == 3
    assert a.root.left.right.value == 6
    assert a.root.left.right.left.value == 5
    assert a.root.left.right.right.value == 7


def test_bst_1_value_starting_at_14_down():
    """Test balancing tree with one value."""
    a = BinarySearchTree()
    a.insert(14)
    assert a.root.value == 14
    assert a.root.right is None
    assert a.root.left is None


def test_bst_2_values_starting_at_14_down():
    """Test balancing tree with two values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    assert a.root.value == 14
    assert a.root.right is None
    assert a.root.left.value == 13


def test_bst_3_values_starting_at_14_down():
    """Test balancing tree with three values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    assert a.root.value == 13
    assert a.root.right.value == 14
    assert a.root.left.value == 12


def test_bst_4_values_starting_at_14_down():
    """Test balancing tree with four values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    assert a.root.value == 13
    assert a.root.right.value == 14
    assert a.root.left.value == 12
    assert a.root.left.left.value == 11


def test_bst_5_values_starting_at_14_down():
    """Test balancing tree with five values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    assert a.root.value == 13
    assert a.root.right.value == 14
    assert a.root.left.value == 11
    assert a.root.left.right.value == 12
    assert a.root.left.left.value == 10


def test_bst_6_values_starting_at_14_down():
    """Test balancing tree with six values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    assert a.root.value == 11
    assert a.root.right.value == 13
    assert a.root.left.value == 10
    assert a.root.right.right.value == 14
    assert a.root.right.left.value == 12
    assert a.root.left.left.value == 9


def test_bst_7_values_starting_at_14_down():
    """Test balancing tree with seven values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    a.insert(8)
    assert a.root.value == 11
    assert a.root.right.value == 13
    assert a.root.left.value == 9
    assert a.root.right.right.value == 14
    assert a.root.left.left.value == 8
    assert a.root.left.right.value == 10
    assert a.root.right.left.value == 12


def test_bst_8_values_starting_at_14_down():
    """Test balancing tree with eight values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    a.insert(8)
    a.insert(7)
    assert a.root.value == 11
    assert a.root.right.value == 13
    assert a.root.left.value == 9
    assert a.root.right.right.value == 14
    assert a.root.left.left.value == 8
    assert a.root.left.right.value == 10
    assert a.root.right.left.value == 12
    assert a.root.left.left.left.value == 7


def test_bst_9_values_starting_at_14_down():
    """Test balancing tree with nine values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    a.insert(8)
    a.insert(7)
    a.insert(6)
    assert a.root.value == 11
    assert a.root.right.value == 13
    assert a.root.left.value == 9
    assert a.root.right.right.value == 14
    assert a.root.left.left.value == 7
    assert a.root.left.right.value == 10
    assert a.root.right.left.value == 12
    assert a.root.left.left.left.value == 6
    assert a.root.left.left.right.value == 8


def test_bst_10_values_starting_at_14_down():
    """Test balancing tree with ten values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    a.insert(8)
    a.insert(7)
    a.insert(6)
    a.insert(5)
    assert a.root.value == 11
    assert a.root.right.value == 13
    assert a.root.right.right.value == 14
    assert a.root.right.left.value == 12
    assert a.root.left.value == 7
    assert a.root.left.left.value == 6
    assert a.root.left.right.value == 9
    assert a.root.left.left.left.value == 5
    assert a.root.left.right.right.value == 10
    assert a.root.left.right.left.value == 8


def test_bst_11_values_starting_at_14_down():
    """Test balancing tree with eleven values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    a.insert(8)
    a.insert(7)
    a.insert(6)
    a.insert(5)
    a.insert(4)
    assert a.root.value == 11
    assert a.root.right.value == 13
    assert a.root.right.right.value == 14
    assert a.root.right.left.value == 12
    assert a.root.left.value == 7
    assert a.root.left.left.value == 5
    assert a.root.left.right.value == 9
    assert a.root.left.left.left.value == 4
    assert a.root.left.right.right.value == 10
    assert a.root.left.right.left.value == 8
    assert a.root.left.left.right.value == 6


def test_bst_12_values_starting_at_14_down():
    """Test balancing tree with twelve values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    a.insert(8)
    a.insert(7)
    a.insert(6)
    a.insert(5)
    a.insert(4)
    a.insert(3)
    assert a.root.value == 7
    assert a.root.right.value == 11
    assert a.root.right.right.value == 13
    assert a.root.right.left.value == 9
    assert a.root.right.left.left.value == 8
    assert a.root.right.left.right.value == 10
    assert a.root.right.right.left.value == 12
    assert a.root.right.right.right.value == 14
    assert a.root.left.value == 5
    assert a.root.left.left.value == 4
    assert a.root.left.right.value == 6
    assert a.root.left.left.left.value == 3


def test_bst_13_values_starting_at_14_down():
    """Test balancing tree with thirteen values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    a.insert(8)
    a.insert(7)
    a.insert(6)
    a.insert(5)
    a.insert(4)
    a.insert(3)
    a.insert(2)
    assert a.root.value == 7
    assert a.root.right.value == 11
    assert a.root.right.right.value == 13
    assert a.root.right.left.value == 9
    assert a.root.right.left.left.value == 8
    assert a.root.right.left.right.value == 10
    assert a.root.right.right.left.value == 12
    assert a.root.right.right.right.value == 14
    assert a.root.left.value == 5
    assert a.root.left.left.value == 3
    assert a.root.left.right.value == 6
    assert a.root.left.left.left.value == 2
    assert a.root.left.left.right.value == 4


def test_bst_14_values_starting_at_14_down():
    """Test balancing tree with fourteen values."""
    a = BinarySearchTree()
    a.insert(14)
    a.insert(13)
    a.insert(12)
    a.insert(11)
    a.insert(10)
    a.insert(9)
    a.insert(8)
    a.insert(7)
    a.insert(6)
    a.insert(5)
    a.insert(4)
    a.insert(3)
    a.insert(2)
    a.insert(1)
    assert a.root.value == 7
    assert a.root.right.value == 11
    assert a.root.right.right.value == 13
    assert a.root.right.left.value == 9
    assert a.root.right.left.left.value == 8
    assert a.root.right.left.right.value == 10
    assert a.root.right.right.left.value == 12
    assert a.root.right.right.right.value == 14
    assert a.root.left.value == 3
    assert a.root.left.left.value == 2
    assert a.root.left.right.value == 5
    assert a.root.left.left.left.value == 1
    assert a.root.left.right.right.value == 6
    assert a.root.left.right.left.value == 4


def test_bst_left_right_basic(filled_bst_rot_2_r_1):
    """Test left right rotation."""
    a = filled_bst_rot_2_r_1
    a.insert(1)
    assert a.root.value == 2
    assert a.root.parent is None
    assert a.root.left.value == 1
    assert a.root.right.value == 3


def test_bst_right_left_basic(filled_bst_rot_2_l_3):
    """Test right left rotation."""
    a = filled_bst_rot_2_l_3
    a.insert(3)
    assert a.root.value == 2
    assert a.root.parent is None
    assert a.root.left.value == 1
    assert a.root.right.value == 3


def test_bst_left_right_root_left_right_add_left(filled_bst_rot_lr_gc_7):
    """Test left right rotation."""
    a = filled_bst_rot_lr_gc_7
    a.insert(7)
    assert a.root.value == 8
    assert a.root.parent is None
    assert a.root.left.value == 5
    assert a.root.left.left.value == 2
    assert a.root.left.right.value == 7
    assert a.root.right.value == 10
    assert a.root.right.left is None
    assert a.root.right.right.value == 12


def test_bst_left_right_root_left_right_add_right(filled_bst_rot_lr_gc_7):
    """Test left right rotation."""
    a = filled_bst_rot_lr_gc_7
    a.insert(9)
    assert a.root.value == 8
    assert a.root.parent is None
    assert a.root.left.value == 5
    assert a.root.left.left.value == 2
    assert a.root.left.right is None
    assert a.root.right.value == 10
    assert a.root.right.left.value == 9
    assert a.root.right.right.value == 12


def test_right_left_root_right_left_add_left(filled_bst_rot_rl):
    """Test right left rotation."""
    a = filled_bst_rot_rl
    a.insert(12)
    assert a.root.value == 13
    assert a.root.parent is None
    assert a.root.left.value == 10
    assert a.root.left.left.value == 5
    assert a.root.left.right.value == 12
    assert a.root.right.value == 15
    assert a.root.right.left is None
    assert a.root.right.right.value == 20


def test_right_left_root_right_left_add_right(filled_bst_rot_rl):
    """Test right left rotation."""
    a = filled_bst_rot_rl
    a.insert(14)
    assert a.root.value == 13
    assert a.root.parent is None
    assert a.root.left.value == 10
    assert a.root.left.left.value == 5
    assert a.root.left.right is None
    assert a.root.right.value == 15
    assert a.root.right.left.value == 14
    assert a.root.right.right.value == 20


def test_bst_double_rotation_one():
    """Test double rotation one."""
    a = BinarySearchTree([10, 5, 15, 13, 20])
    a.insert(12)
    assert a.root.value == 13
    assert a.root.right.value == 15
    assert a.root.left.value == 10
    assert a.root.right.right.value == 20
    assert a.root.left.left.value == 5
    assert a.root.left.right.value == 12


def test_bst_double_rotation_two():
    """Test double rotation one."""
    a = BinarySearchTree([15, 10, 20, 5, 13])
    a.insert(14)
    assert a.root.value == 13
    assert a.root.right.value == 15
    assert a.root.left.value == 10
    assert a.root.right.right.value == 20
    assert a.root.right.left.value == 14
    assert a.root.left.left.value == 5
