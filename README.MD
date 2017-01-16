#Summary

The assignment was to implement a [Deque](https://codefellows.github.io/sea-python-401d5/assignments/deque.html)
in Python containing 6 methods:


* append():       Append a Node with given value to the tail.
* appendleft():   Push a Node with given value to the head.
* pop():          Remove the node from the head, return the value.
* popleft():      Remove the node from the tail, return the value.
* peek():         Return the value from the tail node.
* peekleft():     Return the value from the head node.


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/queue.html



# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing |
| -----------------------  | ----- | ---- | ----- | ------- |
| dbl_linked_list.py       |  75   |  0   | 100%  |         |
| deque.py                 |  32   |  0   | 100%  |         |
| linked_list.py           |  50   |  0   |  96%  |  80-81  |
| queue.py                 |  22   |  2   | 91%   |  47, 51 |
| stack.py                 |   8   |  0   | 100%  |         |
| test_dbl_linked_list.py  |  185  |  0   | 100%  |         |
| test_deque.py            |  23   |  0   | 100%  |         |
| test_linked_list.py      |  73   |  0   |  95%  |         |
| test_queue.py            |  87   |  0   | 100%  |         |
| test_stack.py            |  48   |  0   | 100%  | 106-109 |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  552  |  8   | 99%   |         |


