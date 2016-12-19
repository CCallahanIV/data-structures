"""This is the test module for the deque module."""
import pytest


@pytest.fixture()
def create_empty_deque():
    """Return an empty deque list."""
    from deque import Deque
    new_deque = Deque()
    return new_deque


def test_creating_an_empty_deque(create_empty_deque):
    """Test creating an empty deque list."""
    assert create_empty_deque._container._size == 0
