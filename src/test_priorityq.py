"""This Module contains testing for the Priority Q."""
import pytest
TEST_SET = [
    [(1, 17), (2, 99), (1, 15), (3, 99), (2, 1), (3, 9)],
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

def test_initialize_with_single_tuple
    

def test_intitalize_with_single_digit

def test_into_empty_with_tuple_and_no_prio

def test_into_empty_with_tuple_and_prio_not_already_there

def insert_val_into_empty_priorty_q(empty_priority_q):
    """The tests inserting into an empty priority queue."""
    new_prq = empty_priority_q
    new_prq.insert((1, 3))
    assert len(empty_priority_q) == 1
    assert empty_priority_q._high_p[0] == 1
    assert empty_priority_q._pdict[0] == 3

def test_insert_into_full_with_single_digit_and_no_prio(filled_priority_q):

def test_insert_into_full_with_tuple_prio_already_there(filled_priority_q):

def test_insert_into_full_prio_already_there(filled_priority_q):

def test_insert_into_full_with_an_iterable(filled_priority_q):

def pop_filled_priorty_q(filled_priority_q):
    """The tests inserting into a filled priority queue."""
    new_fprq = filled_priority_q
    val = new_fprq.pop()
    assert len(empty_priority_q) == 5
    assert filled_priority_q._high_p[0] == 1
    assert val == 17
    assert filled_priority_q.peek() == 15

def test_pop_on_empty_priority_q(empty_priority_q):

def test_pop_on_filled_until_empty(filled_priority_q):

def test_peek_on_empty(empty_priority_q):

def test_peek_on_filled(filled_priority_q):
