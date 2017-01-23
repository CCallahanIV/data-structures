"""Hashing functions."""


class AddHash(object):
    """
    Hash using a basic additive function.

    __init__: set initial state of empty hash table.

    get: return a value attached to the given key.

    set: add a value to the table at the given key.

    _hash: additive hash on a key value to return a number as a key.
    """

    def __init__(self, slots):
        """Set starting table values."""
        self.slots = slots
        self.table = {}
        for i in range(slots):
            self.table[i] = []

    def get(self, key):
        """Return a value stored with given key."""
        return self.table[self._hash(key)]

    def set(self, key, val):
        """Store val at key in the table."""
        if not isinstance(key, str):
            raise TypeError('key must be type str')
        self.table[self._hash(key)].append(val)
        return None

    def _hash(self, key):
        hash_total = 0

        for letter in key:
            hash_total += ord(letter)

        return hash_total % self.slots


class FNVHash(object):
    """
    Hash using a Fowler/Noll/Vo function.

    __init__: set initial state of empty hash table.

    get: return a value attached to the given key.

    set: add a value to the table at the given key.

    _hash: additive hash on a key value to return a number as a key.
    """

    def __init__(self, slots):
        """Set starting table values."""
        self.slots = slots
        self.table = {}
        for i in range(slots):
            self.table[i] = []

    def get(self, key):
        """Return a value stored with given key."""
        return self.table[self._hash(key)]

    def set(self, key, val):
        """Store val at key in the table."""
        if not isinstance(key, str):
            raise TypeError('key must be type str')
        self.table[self._hash(key)].append(val)
        return None

    def _hash(self, key):
        hash_total = 2166136261

        for letter in key:
            hash_total = (hash_total * 16777619) ^ ord(letter)

        return hash_total % self.slots
