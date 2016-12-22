# """This module contains the tests for the binary heap."""

# import pytest

# PUSH_TABLE = [
#     [4.5, [1, 3, 5, 4, 6, 7, 9, 4.5]]
#     [3.5, [1, 3, 5, 3.5, 6, 7, 9, 4]]
#     [2.5, [1, 2.5, 5, 3, 6, 7, 9, 4]]
#     [0.5, [0.5, 1, 5, 3, 6, 7, 9, 4]]
#     [0, [1, 5, 3, 6, 7, 9, 4]]
# ]


# @pytest.fixture
# def create_filled_bin_heap():
#     """Create a filled min bin heap."""
#     from binheap import BinHeap
#     filled_heap = BinHeap([1, 3, 5, 4, 6, 7, 9])
#     return filled_heap


# def test_push_to_end_of_an_empty_bin_heap():
#     """Test pushing val to end of an empty bin heap."""
#     from binheap import BinHeap
#     new_list = BinHeap()
#     assert len(new_list.push(4)) == 1


# @pytest.mark.usefixtures("create_filled_bin_heap")
# @pytest.mark.parametrize("val, result", PUSH_TABLE)
# def test_push_to_end_of_a_filled_bin_heap(val, result):
#     """Test pushing val to end of a filled bin heap."""
#     new_filled_list = create_filled_bin_heap()
#     new_filled_list.push(val)
#     assert new_filled_list._tree_list == result


# def test_pop_off_bin_heap(create_filled_bin_heap):
#     """Test popping root value off the top of a filled bin heap."""
#     new_filled_list = create_filled_bin_heap()
#     new_filled_list.pop()
#     assert new_filled_list[0] == 3
