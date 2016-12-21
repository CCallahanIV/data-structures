"""This module contains an implementation of a binary heap."""


class BinHeap(object):
    """Define a Binary Heap Object."""
    def __init__(self, maybe_an_iterable=None):
        """Initialize a Binary Heap Object."""
        self._tree_list = []
        if maybe_an_iterable:
            try:
                for value in maybe_an_iterable:
                    self.push(value)
            except TypeError:
                self.push(maybe_an_iterable)

    def pop(self):
        """Pop the head of the heap off."""
        self._tree_list[-1], self._tree_list[0] = self._tree_list[0], self._tree_list[-1]
        val = self._tree_list.pop()
        i = 0
        while (i * 2) < len(self._tree_list) - 1:
            swap_child = self._eval_child(i)
            if self._tree_list[swap_child] < self._tree_list[i]:
                self._tree_list[swap_child], self._tree_list[i] = self._tree_list[i], self._tree_list[swap_child]
            i = swap_child
        return val

    def _eval_child(self, i):
        """Evaluate which child should be swapped for a given index."""
        if i * 2 + 2 > len(self._tree_list) - 1:
            return i * 2 + 1
        else:
            if self._tree_list[i * 2 + 1] < self._tree_list[i * 2 + 2]:
                return i * 2 + 1
            else:
                return i * 2 + 2

    def push(self, value):
        """Add a Node to the bottom of the heap with given value."""
        self._tree_list.append(value)
        if len(self._tree_list) > 1:
            i = len(self._tree_list) - 1
            while i // 2 > 0:
                parent = i // 2
                if self._tree_list[i] < self._tree_list[parent]:
                    self._tree_list[i], self._tree_list[parent] = self._tree_list[parent], self._tree_list[i]
                    i = parent
                break

    def __len__(self):
        """Return length (size) of heap."""
        return len(self._tree_list)
