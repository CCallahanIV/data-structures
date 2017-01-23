"""Test additive and FNV hash."""

import pytest

@pytest.fixture
def new_add():
    from hash import AddHash
    return AddHash(slots)