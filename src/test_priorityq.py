"""This Module contains testing for the Priority Q."""
import pytest
TEST_SET = [
    [(17, 1), (99, 2), (15, 1), (99, 3), (1, 2), (9, 3)],
]


@pytest.fixture
def empty_priority_q():
    """Thie fixture creates and empty priority queue."""
    from priorityq import PriorityQ
    new_pq = PriorityQ()
    return new_pq


@pytest.fixture(scope="module", params=TEST_SET)
def filled_priority_q(request):
    """The fixture creates a filled priority queue."""
    from priorityq import PriorityQ
    new_pq = PriorityQ(TEST_SET)
    return new_pq


def test_creation_of_empty_priority_q(empty_priority_q):
    """The creates an empty queue and tests the size."""
    assert len(empty_priority_q) == 0
    assert len(empty_priority_q._high_p) == 0
    assert len(empty_priority_q._pdict) == 0

def test_initialize_with_single_tuple():
    """The test initializes priority q with a single tuple."""
    from priorityq import PriorityQ
    new_pq = PriorityQ((3,2))
    assert len(new_pq) == 1
    assert new_pq._high_p == 2
    assert new_pq.peek() == 3
    

def test_intitalize_with_single_digit():
    """The test initialized a prio q with a single digit."""
    from priorityq import PriorityQ
    with pytest.raises(TypeError):
        new_pq = PriorityQ(3)


def test_insert_empty_with_val_and_no_prio(empty_priority_q):
    """The test inserts val w/o prio to empty list."""
    in_epq = empty_priority_q.insert(4)
    assert in_epq._high_p == 0
    assert in_epq._pdict[0].peek() == 4


def test_insert_filled_with_val_and_prio_where_prio_not_already_there(filled_priority_q):
    """The test inserts with val and prio, where prio not already there."""
    in_fpq = filled_priority_q.insert(7, 4)
    assert in_fpq._pdict[4].peek() == 7


def insert_val_into_empty_priorty_q(empty_priority_q):
    """The tests inserting into an empty priority queue."""
    new_prq = empty_priority_q
    new_prq.insert(3, 1)
    assert len(empty_priority_q) == 1
    assert empty_priority_q._high_p[0] == 3
    assert empty_priority_q._pdict[0] == 3


def test_insert_into_full_prio_already_there(filled_priority_q):
    """Test inserting into a filled priority q, with priority already present."""
    old_len = len(filled_priority_q)
    filled_priority_q.insert("something", 1)
    assert len(filled_priority_q) = old_len + 1
    assert filled_priority_q.peek() == 17


def test_insert_into_full_with_an_iterable(filled_priority_q):
    """Test attempting to insert into a priority q with an iterable."""
    with pytest.raises(TypeError):
        filled_priority_q.insert([1, 2, 3])


def pop_filled_priorty_q(filled_priority_q):
    """The tests inserting into a filled priority queue."""
    new_fprq = filled_priority_q
    val = new_fprq.pop()
    assert len(empty_priority_q) == 5
    assert filled_priority_q._high_p[0] == 1
    assert val == 17
    assert filled_priority_q.peek() == 15


def test_pop_on_empty_priority_q(empty_priority_q):
    """Test popping on an empty priority q."""
    with pytest.raises(IndexError):
        empty_priority_q.pop()


def test_pop_on_filled_until_empty(filled_priority_q):
    """Test pop on filled Priority Q until empty."""
    expected = [17, 15, 2, 99, 1, 99, 9]
    for i in len(filled_priority_q):
        assert filled_priority_q.pop() == expected[i]
    assert len(filled_priority_q) == 0
    assert self._high_p is None


def test_peek_on_empty(empty_priority_q):
    """Test peek() on an empty priority Q, should return None."""
    assert empty_priority_q.peek() is None


def test_peek_on_filled(filled_priority_q):
    """Test peek() on a filled priorityq."""
    assert filled_priority_q.peek() == 17
