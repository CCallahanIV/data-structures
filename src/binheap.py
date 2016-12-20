"""This module contains an implementation of a binary heap."""


class TreeNode(object):
    """Define a Node object for use in binary trees."""
    def __init__(self, value=None, parent=None, left=None, right=None):
        """Initialize a TreeNode Object."""
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class BinHeap(object):
    """Define a Binary Heap Object."""
    def __init__(self, maybe_an_iterable=None):
        """Initialize a Binary Heap Object."""
        self._tree_list = []
        self._size = len(self._tree_list)

    def pop(self):
        """Pop the head of the heap off."""
        pass

    def push(self, value):
        """Add a Node to the bottom of the heap with given value."""
        pass

