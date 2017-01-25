
# HASH TABLE (HT)
#
# CodeFellows 401d5
# Submission Date:
#
# Authors:  Colin Lamont <https://github.com/chamberi>
#           Ben Shields <https://github.com/iamrobinhood12345>
#
# URL:


"""
The HashTable is a data structure that implements an
assosiative array. The structure maps keys to values
in such a way that values may be accessed in O(1) time.
This is done through use of a hashing function.
The hashing function maps the content of the key to
a specific bucket. As the content of the key always
maps to a specific hash value, the key's value may
be accessed quickly.
"""


class HashTable(object):
    """Hash Table."""

    """self._num_buckets - the number of buckets in the Hash Table."""
    """get(key) - should return the value stored with the given key."""
    """set(key, val) - store the given val using the given key."""
    """_hash(key) - hash the key provided (note that this is an internal api)."""

    def __init__(self, type='additive'):
        """Init function for the Hash Table class."""
        self._num_buckets = 1000
        self._container = [[] for i in range(0, self._num_buckets)]

    def get(self, key):
        """Return the value corresponding to this key in the hash table."""
        hashed_value = self._hash(key)
        for each in self._container[hashed_value]:
            if each[0] == key:
                return each[1]
        return 'Key not in hash table.'

    def set(self, key, val):
        """Place the key value pair in the hash table."""
        hashed_value = self._hash(key)
        for each in self._container[hashed_value]:
            if each[0] == key:
                (self._container[hashed_value]).remove(each)
        (self._container[hashed_value]).append((key, val))

    def _hash(self, key):
        """Additive hash function."""
        return sum([ord(each) for each in key]) % self._num_buckets
