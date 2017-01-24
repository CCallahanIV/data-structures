
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
The Mailroom module allows the user to
track donations and format emails for donors.
The user can write tailored thank you emails
given donor names and donation amounts.
The user can create a report that is
a list of donor names and their corresponding donation
histories, arranged by in order of the total amount
donated.
The user can add a donor name to this list.
The user can quit the program from Main Menu, and
may return to Main Menu at any time.
"""


class HashTable(object):
    """Hash Table."""

    """get(key) - should return the value stored with the given key"""
    """set(key, val) - should store the given val using the given key"""
    """_hash(key) - should hash the key provided (note that this is an internal api)"""

    def __init__(self):
        """Init function for the Hash Table class."""
        self._container = []
        self._num_buckets = 1000
        for i in range(0, self._num_buckets):
            self._container.append([])

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
        (self._container[hashed_value]).append((key, val))
        return

    def _hash(self, key):
        """Docstring."""
        num = 0
        for each in key:
            num += ord(each)
        return num % self._num_buckets
