"""This module contains an implementation of the PriorityQ."""

from queue_ds import Queue


class PriorityQ(object):
    """Define a PriorityQ object."""

    def __init__(self, maybe_an_iterable=None):
        """Initialize a PriorityQ object."""
        self._plist = []
        self._pdict = {}
        self._size = 0
        if hasattr(maybe_an_iterable, "__iter__"):
            for item in maybe_an_iterable:
                insert(item)
        elif maybe_an_iterable is not None:
            insert(maybe_an_iterable)

    def insert(self, value):
        """Insert a given value into the appropriate place in the PriorityQ."""
        pass

    def pop(self):
        """Remove the item with greatest priority and return its value."""
        pass

    def peek(self):
        """Return the value of the item with greatest priority, do not remove it."""
        pass
