"""This module contains the deque data structure."""

from dbl_linked_list import DblLinkedList


class Deque(object):
    """This is the Deque data structure."""

    def __init__(self):
        """Initialize a deque data structure."""
        pass

    def append(self, val):
        """Append a node with given value to the tail."""
        pass

    def appendleft(self, val):
        """Append a node with given value to the head."""
        pass

    def pop(self):
        """Remove the node from the tail and return the value."""
        pass

    def popleft(self):
        """Remove the node from the head and return the value."""
        pass

    def peek(self):
        """Give the value for the tail node."""
        pass

    def peekleft(self):
        """Give the value for the head node."""
        pass

    def size(self):
        """Return the length of the deque."""

    def __len__(self):
        """Call the size method."""
        return self.size()
