[![Build Status](https://travis-ci.org/chamberi/data-structures.svg?branch=master)](https://travis-ci.org/chamberi/data-structures)
#Summary

Merge Sort takes a list and re-orders it so that the items in the list are arranged lowest to highest.
Merge method compares two lists and re-arranges to form a new list from lowest to highest.
Random_list returns a list of random numbers from 0 to 300 of random size less than 300.
Best_list returnd a list of random numbers of random size less than 300 in ascending order.
Worst_list returns a list of randon numbers of random size less than 300 in descending order.

Timeit Information:


number of runs: 3
random merge_sort_timed: [1.0025185380363837, 1.038343450985849, 1.0102136129280552]
average:  1.017025200650096

number of runs: 3
best case merge_sort_timed: [0.7397163880523294, 0.734698642976582, 0.7407603049650788]
average:  0.7383917786646634
number of runs: 3

worst case merge_sort_timed: [0.8237005720147863, 0.8032845410052687, 0.7924857450416312]
average:  0.806490286020562


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
