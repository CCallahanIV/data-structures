"""This module contains the deque data structure."""

from dbl_linked_list import DblLinkedList


class Deque(object):
    """This is the Deque data structure."""

    def __init__(self, maybe_an_iterable=None):
        """Initialize a deque data structure."""
        try:
            self._container = DblLinkedList(maybe_an_iterable)
        except TypeError:
            self._container = DblLinkedList(maybe_an_iterable)

    def append(self, val):
        """Append a node with given value to the tail."""
        self._container.append(val)

    def appendleft(self, val):
        """Append a node with given value to the head."""
        self._container.push(val)

    def pop(self):
        """Remove the node from the tail and return the value."""
        try:
            return self._container.shift()
        except IndexError:
            raise IndexError("Cannot pop from empty Deque.")

    def popleft(self):
        """Remove the node from the head and return the value."""
        try:
            self._container.pop()
        except IndexError:
            raise IndexError("Cannot popleft from empty Deque.")

    def peek(self):
        """Give the value for the tail node."""
        pass

    def peekleft(self):
        """Give the value for the head node."""
        pass

    def size(self):
        """Return the length of the deque."""
        return self._container._size

    def __len__(self):
        """Call the size method."""
        return self.size()
