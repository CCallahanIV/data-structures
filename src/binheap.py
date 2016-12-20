"""This module contains an implementation of a binary heap."""


class BinHeap(object):
    """Define a Binary Heap Object."""
    def __init__(self, maybe_an_iterable=None):
        """Initialize a Binary Heap Object."""
        self._tree_list = []

    def pop(self):
        """Pop the head of the heap off."""
        pass

    def push(self, value):
        """Add a Node to the bottom of the heap with given value."""
        self._tree_list.append(value)
