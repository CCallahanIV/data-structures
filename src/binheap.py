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
        if len(self._tree_list) > 1:
            i = len(self._tree_list) - 1
            while i > 0:
                parent = int((i - 1) / 2)
                if self._tree_list[i] < self._tree_list[parent]:
                    self._tree_list[i], self._tree_list[parent] = self._tree_list[parent], self._tree_list[i]
                    i = parent
                break

    def __len__(self):
        """Return length (size) of heap."""
        return len(self._tree_list)
