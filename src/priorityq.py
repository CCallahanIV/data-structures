"""This module contains an implementation of the PriorityQ."""

from queue_ds import Queue


class PriorityQ(object):
    """Define a PriorityQ object."""

    def __init__(self, maybe_an_iterable=None):
        """Initialize a PriorityQ object."""
        self._high_p = None
        self._pdict = {}
        self._size = 0
        if maybe_an_iterable is not None:
            self.insert(maybe_an_iterable)

    def insert(self, item):
        """Insert a given item into the appropriate place in the PriorityQ."""
        try:
            self._pdict[item[0]].enqueue(item[1])
        except KeyError:
            if self._high_p is None or item[0] < self._high_p:
                self._high_p = item[0]
            self._pdict[item[0]] = Queue([item[1]])
        self._size += 1

    def pop(self):
        """Remove the item with greatest priority and return its value."""
        val = self._pdict[self._high_p].dequeue()
            if len(self._pdict[self._high_p]]) == 0:
                del self._pdict[_high_p]
                self._high_p = min(self._pdict.keys())
        return val 

    def peek(self):
        """Return the value of the item with greatest priority, do not remove it."""
        return self._pdict[self._high_p].peek()

    def __len__(self):
        """Return the total size of the PrioritQ."""
        return self._size
