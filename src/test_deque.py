"""This is the test module for the deque module."""
import pytest


TEST_ITER = [1, 2, 3, 4, 5]


@pytest.fixture()
def create_filled_deque():
    """The fixture creates the filled deque list for testing purposes."""
    from deque import Deque
    new_filled_deque = Deque(TEST_ITER)
    return new_filled_deque


@pytest.fixture()
def create_empty_deque():
    """Return an empty deque list."""
    from deque import Deque
    new_deque = Deque()
    return new_deque


def test_creating_an_empty_deque(create_empty_deque):
    """Test creating an empty deque list."""
    assert create_empty_deque._container._size == 0


def test_creating_a_filled_deque(create_filled_deque):
    """Test creating a filled deque list."""
    assert create_filled_deque._container.head.value == 5
    assert create_filled_deque._container.tail.value == 1
    assert create_filled_deque._container._size == 5
