"""Test additive and FNV hash."""

# import pytest
import os

# @pytest.fixture
# def small_add():
#     from hash import AddHash
#     return AddHash(11)


def test_add_hash():
    """Test the additive hash table."""
    from hash import AddHash
    path = os.path.abspath('/usr/share/dict/words')
    with open(path, 'r') as f:
        data = f.read()
    keys = data.split('\n')
    a_hash = AddHash(len(keys))
    for key in keys:
        a_hash.set(key, key)

    for key in keys:
        assert key == a_hash.get(key)


def test_fnv_hash():
    """Test the additive hash table."""
    from hash import FNVHash
    path = os.path.abspath('/usr/share/dict/words')
    with open(path, 'r') as f:
        data = f.read()
    keys = data.split('\n')
    f_hash = FNVHash(len(keys))
    for key in keys:
        f_hash.set(key, key)

    for key in keys:
        assert key == f_hash.get(key)
