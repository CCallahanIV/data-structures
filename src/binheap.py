"""This module contains an implementation of a binary heap."""


class BinHeap(object):
    """Define a Binary Heap Object."""

    def __init__(self, maybe_an_iterable=None, min_heap=True):
        """Initialize a Binary Heap Object."""
        self._tree_list = []
        self.min_heap = min_heap
        if maybe_an_iterable:
            try:
                for value in maybe_an_iterable:
                    self.push(value)
            except TypeError:
                self.push(maybe_an_iterable)
        if self.min_heap is False:
            print("Initialized as Max Heap.")

    def pop(self):
        """Pop the head of the heap off."""
        if len(self._tree_list) == 0:
            raise IndexError("Cannot pop from empty Binary Heap.")
        self._swap(0, -1)
        val = self._tree_list.pop()
        i = 0
        while (i * 2) < len(self._tree_list) - 1:
            swap_child = self._eval_child(i)
            if self._tree_list[swap_child] < self._tree_list[i] if self.min_heap else self._tree_list[swap_child] > self._tree_list[i]:
                self._swap(swap_child, i)
            i = swap_child
        return val

    def push(self, value):
        """Add a Node to the bottom of the heap with given value."""
        self._tree_list.append(value)
        if len(self._tree_list) > 1:
            i = len(self._tree_list) - 1
            while i > 0:
                parent = (i - 1) // 2
                if self._tree_list[i] < self._tree_list[parent] if self.min_heap else self._tree_list[i] > self._tree_list[parent]:
                    self._swap(parent, i)

                i = parent

    def _eval_child(self, i):
        """Evaluate which child should be swapped for a given index."""
        if i * 2 + 2 > len(self._tree_list) - 1:
            return i * 2 + 1
        else:
            if self._tree_list[i * 2 + 1] < self._tree_list[i * 2 + 2] if self.min_heap else self._tree_list[i * 2 + 1] > self._tree_list[i * 2 + 2]:
                return i * 2 + 1
            else:
                return i * 2 + 2

    def _swap(self, a, b):
        """Swap list items at given indexes."""
        self._tree_list[a], self._tree_list[b] = self._tree_list[b], self._tree_list[a]

    def __len__(self):
        """Return length (size) of heap."""
        return len(self._tree_list)
