"""This module contains an implementation of the PriorityQ."""

from queue_ds import Queue


class PriorityQ(object):
    """Define a PriorityQ object."""

    def __init__(self, maybe_an_iterable=None):
        """Initialize a PriorityQ object."""
        self._high_p = None
        self._pdict = {}
        self._size = 0
        if maybe_an_iterable:
            try:
                self.insert(maybe_an_iterable[0], maybe_an_iterable[1])
            except TypeError:
                try:
                    for item in maybe_an_iterable:
                        self.insert(item[0], item[1])
                except TypeError:
                    raise TypeError("Initialize PriorityQ with list of Tuples in format: [(value, priority), ...]")

    def insert(self, value, priority=0):
        """Insert a given item into the appropriate place in the PriorityQ."""
        if type(priority) != int or type(value) in [list, tuple, dict, set]:
            raise TypeError("Improper function call.  Call insert as .insert(val[, priority])")

        self._pdict.setdefault(priority, Queue()).enqueue(value)
        if self._high_p is None or priority < self._high_p:
            self._high_p = priority
        self._size += 1

    def pop(self):
        """Remove the item with greatest priority and return its value."""
        try:
            val = self._pdict[self._high_p].dequeue()
            if len(self._pdict[self._high_p]) == 0:
                del self._pdict[self._high_p]
                try:
                    self._high_p = min(self._pdict.keys())
                except ValueError:
                    self._high_p = None
            self._size -= 1
            return val
        except KeyError:
            raise IndexError("Cannot pop from empty Priority Q.")

    def peek(self):
        """Return the value of the item with greatest priority, do not remove it."""
        try:
            return self._pdict[self._high_p].peek()
        except KeyError:
            return None

    def __len__(self):
        """Return the total size of the PrioritQ."""
        return self._size
