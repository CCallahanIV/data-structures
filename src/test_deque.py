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


def test_create_deque_with_string():
    """Test create deque with string, should create node for each char."""
    from deque import Deque
    nd = Deque("four")
    assert len(nd) == 4


def test_create_deque_w_empty_list():
    """Test create deque with [], should create one node."""
    from deque import Deque
    l = []
    nd = Deque(l)
    assert len(nd) == 0


def test_create_deque_single_item():
    """Test create deque with single node."""
    from deque import Deque
    nd = Deque(1)
    assert len(nd) == 1
    assert nd._container.head.value == 1
    assert nd._container.tail.value == 1


def test_append_adding_node_to_tail(create_empty_deque):
    """Test adding a new node to the tail of an empty deque."""
    create_empty_deque.append(6)
    assert create_empty_deque._container.tail.value == 6
    assert create_empty_deque._container.head.value == 6
    assert create_empty_deque._container._size == 1


def test_append_on_a_filled_deque_list(create_filled_deque):
    """Test adding a new node to end of a filled deque."""
    create_filled_deque.append(6)
    assert create_filled_deque._container.tail.value == 6
    assert create_filled_deque._container._size == 6


def test_appendleft_on_an_empty_deque(create_empty_deque):
    """Test adding a node to front of a deque."""
    create_empty_deque.appendleft(6)
    assert create_empty_deque._container.head.value == 6
    assert create_empty_deque._container._size == 1


def test_appendleft_on_a_filled_deque(create_filled_deque):
    """Test adding a node to the front of a filled deque."""
    create_filled_deque.appendleft(6)
    assert create_filled_deque._container.head.value == 6
    assert create_filled_deque._container._size == 6


def test_pop_on_filled_deque(create_filled_deque):
    """Test pop method on filled deque."""
    assert create_filled_deque.pop() == 1
    assert create_filled_deque._container.tail.value == 2
    assert create_filled_deque._container._size == 4


def test_pop_on_empty_deque(create_empty_deque):
    """Test pop on empty deque, should raise exception."""
    with pytest.raises(IndexError):
        create_empty_deque.pop()


def test_pop_from_full_to_empty_deque(create_filled_deque):
    """Test pop on full deque until empty, verify head, tail are none."""
    for i in range(len(create_filled_deque)):
        create_filled_deque.pop()

    assert create_filled_deque._container.head is None
    assert create_filled_deque._container.tail is None
    assert create_filled_deque._container._size == 0


def test_popleft_on_filled_deque(create_filled_deque):
    """Test popleft on filled deque."""
    assert create_filled_deque.popleft() == 5
    assert create_filled_deque._container.head.value == 4
    assert create_filled_deque._container._size == 4


def test_popleft_on_empty_deque(create_empty_deque):
    """Test popleft on an empty deque, should raise IndexError."""
    with pytest.raises(IndexError):
        create_empty_deque.popleft()


def test_popleft_from_full_to_empty_deque(create_filled_deque):
    """Test popleft on full deque until empty, verify head, tail are none."""
    for i in range(len(create_filled_deque)):
        create_filled_deque.popleft()

    assert create_filled_deque._container.head is None
    assert create_filled_deque._container.tail is None
    assert create_filled_deque._container._size == 0


def test_peek_on_filled_deque(create_filled_deque):
    """Test peek on filled deque to return tail value."""
    assert create_filled_deque.peek() == 1


def test_peek_on_an_empty_deque(create_empty_deque):
    """Test peek on an empty queue to raise exception."""
    assert create_empty_deque.peek() is None


def test_peekleft_on_filled_deque(create_filled_deque):
    """Test peekleft on filled deque to return head value."""
    assert create_filled_deque.peekleft() == 5


def test_peekleft_on_empty_deque(create_empty_deque):
    """Test peekleft on an empty deque to return head value."""
    assert create_empty_deque.peekleft() is None


def test_size_on_a_filled_deque(create_filled_deque):
    """Test size method to return length on a filled deque."""
    assert create_filled_deque._container._size == 5


def test_size_on_an_empty_deque(create_empty_deque):
    """Test size method to return length on an empty deque."""
    assert create_empty_deque._container._size == 0
