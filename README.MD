#Summary

The HashTable is a data structure that implements an
assosiative array. The structure maps keys to values
in such a way that values may be accessed in O(1) time.
This is done through use of a hashing function.
The hashing function maps the content of the key to
a specific bucket. As the content of the key always
maps to a specific hash value, the key's value may
be accessed quickly.

    - get(key) - should return the value stored with the given key
    - set(key, val) - should store the given val using the given key
    - _hash(key) - should hash the key provided (note that this is an internal api)


# Coverage:

-----------------------------------------------------------
---------- coverage: platform darwin, python 2.7.12-final-0 ----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
src/hash_table.py                47      2    96%   54, 58
-----------------------------------------------------------
---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
src/hash_table.py                47      2    96%   54, 58
-----------------------------------------------------------

Gen Primes function used:
Sieve of Eratosthenes
Code by David Eppstein, UC Irvine, 28 Feb 2002
http://code.activestate.com/recipes/117119/
