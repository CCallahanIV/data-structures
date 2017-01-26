
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

    def __init__(self, hash_type='additive'):
        """Init function for the Hash Table class."""
        self._num_buckets = 50000
        self._container = [[] for i in range(0, self._num_buckets)]
        self._type = hash_type

    def get(self, key):
        """Return the value corresponding to this key in the hash table."""
        hashed_value = self._hash(key)
        for each in self._container[hashed_value]:
            if each[0] == key:
                return each[1]
        return 'Key not in hash table.'

    def set(self, key, val):
        """Place the key value pair in the hash table."""
        if type(key) is not str:
            return 'Keys must be strings.'
        hashed_value = self._hash(key)
        for each in self._container[hashed_value]:
            if each[0] == key:
                (self._container[hashed_value]).remove(each)
        (self._container[hashed_value]).append((key, val))

    def _hash(self, key):
        """Additive hash function."""
        if self._type == 'additive':
            return self._additive_hash(key)
        if self._type == 'colin-ben':
            return self._colin_ben_hash(key)

    def _additive_hash(self, key):
        return sum([ord(each) for each in key]) % self._num_buckets

    def _colin_ben_hash(self, key):
        ords = []
        sieve = gen_primes()
        for each in key:
            num = ord(each)
            if ord(each) % 2 == 0:
                num = int(str(ord(each))[::-1])
            ords.append([num, next(sieve)])
        a_sum = sum([each[0] * each[1] for each in ords])
        return a_sum % self._num_buckets

    # def _colin_ben_hash(self, key):
    #     ords = []
    #     sieve = gen_primes()
    #     for each in key:
    #         num = ord(each)
    #         if ord(each) % 2 == 0:
    #             num = int(str(ord(each))[::-1])
    #         ords.append([num, next(sieve)])
    #     a_sum = sum([(each[0] << next(sieve)) * (each[1] << next(sieve)) for each in ords])
    #     return a_sum % self._num_buckets

# def genPrimes():
#     def isPrime(n):
#         if n % 2 == 0: return n == 2
#         d = 3
#         while d * d <= n:
#             if n % d == 0: return False
#             d += 2
#         return True
#     def init(): # change to Sieve of Eratosthenes
#         ps, qs, sieve = [], [], [True] * 50000
#         p, m = 3, 0
#         while p * p <= 100000:
#             if isPrime(p):
#                 ps.insert(0, p)
#                 qs.insert(0, p + (p-1) / 2)
#                 m += 1
#             p += 2
#         for i in xrange(m):
#             for j in xrange(qs[i], 50000, ps[i]):
#                 sieve[j] = False
#         return m, ps, qs, sieve
#     def advance(m, ps, qs, sieve, bottom):
#         for i in xrange(50000): sieve[i] = True
#         for i in xrange(m):
#             qs[i] = (qs[i] - 50000) % ps[i]
#         p = ps[0] + 2
#         while p * p <= bottom + 100000:
#             if isPrime(p):
#                 ps.insert(0, p)
#                 qs.insert(0, (p*p - bottom - 1)/2)
#                 m += 1
#             p += 2
#         for i in xrange(m):
#             for j in xrange(qs[i], 50000, ps[i]):
#                 sieve[j] = False
#         return m, ps, qs, sieve
#     m, ps, qs, sieve = init()
#     bottom, i = 0, 1
#     yield 2
#     while True:
#         if i == 50000:
#             bottom = bottom + 100000
#             m, ps, qs, sieve = advance(m, ps, qs, sieve, bottom)
#             i = 0
#         elif sieve[i]:
#             yield bottom + i + i + 1
#             i += 1
#         else: i += 1

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
