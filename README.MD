[![Build Status](https://travis-ci.org/chamberi/data-structures.svg?branch=master)](https://travis-ci.org/chamberi/data-structures)
#Summary

Merge Sort takes a list and re-orders it so that the items in the list are arranged lowest to highest.
Merge method compares two lists and re-arranges to form a new list from lowest to highest.
Random_list returns a list of random numbers from 0 to 300 of random size less than 300.
Best_list returnd a list of random numbers of random size less than 300 in ascending order.
Worst_list returns a list of randon numbers of random size less than 300 in descending order.

Timeit Information:


number of runs: 3
random merge_sort_timed: [2.029730997979641, 2.009656429057941, 2.0230366070754826]
average:  2.0208080113710216

number of runs: 3
best case merge_sort_timed: [0.9284612570190802, 0.939503213041462, 0.9183095849584788]
average:  0.9287580183396736

number of runs: 3
worst case merge_sort_timed: [1.1671109580202028, 1.1538064640481025, 1.159422929980792]
average:  1.1601134506830324


test_merge_sort.py ............................

---------- coverage: platform darwin, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
merge_sort.py                58     16    72%   76-97

test_merge_sort.py ............................

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
merge_sort.py                58     16    72%   76-97
