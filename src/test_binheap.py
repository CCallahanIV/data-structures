"""This module contains the tests for the binary heap."""

import pytest


@pytest.fixture
def create_empty_tree_node():
    """create an empty tree node object."""
    from binheap import TreeNode
    node = TreeNode()
    return node


def test_create_empty_tree_node(create_empty_tree_node):
    """Test creation of an empty Tree Node."""
    node = create_empty_tree_node
    assert node.value is None
    assert node.parent is None
    assert node.left is None
    assert node.right is None
