"""Test Module for Binary Search Tree."""


# def test_insert1():
#     from bst import BinarySearchTree
#     # import pdb; pdb.set_trace()
#     a = BinarySearchTree()
#     a.insert(5)
#     assert a._bstdict[5]

def test_insert2():
    from bst import BinarySearchTree
    a = BinarySearchTree()
    import pdb; pdb.set_trace()
    a.insert(5)
    a.insert(10)
    assert a._bstdict[5] == [None, 10]

# def test_insert3():
#     from bst import BinarySearchTree
#     a = BinarySearchTree()
#     a.insert(8)
#     a.insert(10)
#     a.insert(3)
#     a.insert(14)
#     a.insert(13)
#     a.insert(1)
#     a.insert(6)
#     a.insert(7)
#     a.insert(4)
#     assert a._bstdict[6] == [4, 7]
#     # assert a[3] == [1, 6]
#     # assert a[14] == [13, "z"]
#     # assert a[8] == [3, 10]
#     # assert a[13] == ["z", "z"]
