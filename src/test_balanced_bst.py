"""Test Module for Balanced Binary Search Tree."""
from balanced_bst import BinarySearchTree
import pytest

BST_ROT_2_R_1 = [3, 2]
BST_ROT_2_L_3 = [1, 2]
BST_ROT_4_R_1 = [5, 6, 4, 2]
BST_ROT_4_LR_2 = [5, 6, 3, 1]
BST_ROT_4_L_12 = [6, 8, 5, 10]
BST_ROT_4_RL_9 = [6, 8, 5, 10]
BST_ROT_5_L_GC_6 = [2, 1, 4, 3, 5]
BST_ROT_5_L_GC_5 = [2, 1, 4, 3, 6]
# BST_ROT_5_R_GC_1 = []
# BST_ROT_5_LR_GC_3 = []

# filled_bst_rot_2_r_1
# filled_bst_rot_2_l_3
# filled_bst_rot_4_r_1
# filled_bst_rot_4_lr_2
# filled_bst_rot_4_r_12
# filled_bst_rot_4_rl_9
# filled_bst_rot_5_l_gc_6
# filled_bst_rot_5_rl_gc_5
# filled_bst_rot_5_r_gc_1
# filled_bst_rot_5_lr_gc_3


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
def filled_bst_rot_4_r_1():
    """Fixture for a 4 node tree for a right rotation with insertion of 1."""
    new_tree = BinarySearchTree(BST_ROT_4_R_1)
    return new_tree


@pytest.fixture
def filled_bst_rot_4_lr_2():
    """Fixture for a 4 node tree for a left-right rotation with insertion of 2."""
    new_tree = BinarySearchTree(BST_ROT_4_LR_2)
    return new_tree


@pytest.fixture
def filled_bst_rot_4_l_12():
    """Fixture for a 4 node tree for a left rotation with insertion of 12."""
    new_tree = BinarySearchTree(BST_ROT_4_L_12)
    return new_tree


@pytest.fixture
def filled_bst_rot_4_rl_9():
    """Fixture for a 4 node tree for a right-left rotation with insertion of 9."""
    new_tree = BinarySearchTree(BST_ROT_4_RL_9)
    return new_tree


@pytest.fixture
def filled_bst_rot_5_l_gc_6():
    """Fixture for a 4 node tree for a right-left rotation with insertion of 9."""
    new_tree = BinarySearchTree(BST_ROT_5_L_GC_6)
    return new_tree


@pytest.fixture
def filled_bst_rot_5_l_gc_5():
    """Fixture for a 4 node tree for a left rotation with insertion of 9."""
    new_tree = BinarySearchTree(BST_ROT_5_L_GC_5)
    return new_tree


# @pytest.fixture
# def filled_bst_rot_5_r_gc_1():
#     """Fixture for a 4 node tree for a right-left rotation with insertion of 9."""
#     new_tree = BinarySearchTree(BST_ROT_5_R_GC_1)
#     return new_tree


# @pytest.fixture
# def filled_bst_rot_5_lr_gc_3():
#     """Fixture for a 4 node tree for a right-left rotation with insertion of 9."""
#     new_tree = BinarySearchTree(BST_ROT_5_LR_GC_3)
#     return new_tree


def test_simple_3_node_right_rotation(filled_bst_rot_2_r_1):
    """Balance bst via right rotation, when adding 1 to tree of 3, 2."""
    a = filled_bst_rot_2_r_1
    a.insert(1)
    assert a.root.value == 2
    assert a.root.right.value == 3
    assert a.root.left.value == 1


def test_simple_3_node_left_rotation(filled_bst_rot_2_l_3):
    """Balance bst via right rotation, when adding 3 to tree of 1, 2."""
    a = filled_bst_rot_2_l_3
    a.insert(3)
    assert a.root.value == 2
    assert a.root.right.value == 3
    assert a.root.left.value == 1

# def test_left_right