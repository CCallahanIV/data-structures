[![Build Status](https://travis-ci.org/chamberi/data-structures.svg?branch=master)](https://travis-ci.org/chamberi/data-structures)
#Summary

quick_sort: picks a pivot, compares the rest of list next to the pivot, creates a lesser and greater list, and recursively calls quick_sort, combining the sorted lists and initial pivot at the end.

_random_list() returns a list of random numbers from 0 to 300 of random size less than 300. 


## Timeit Information:

number of runs: 3
random quick_sort_timed: [0.41075075999833643, 0.39770520699676126, 0.38073374499799684]
average:  0.39639657066436484
number of runs: 3

arranged case quick_sort_timed: [2.141874284017831, 2.1192383560119197, 2.095355052035302]
average:  2.1188225640216842
number of runs: 3

reversed case quick_sort_timed: [2.0951970440219156, 2.0876480030128732, 2.0934092969982885]
average:  2.0920847813443593

## Tests and Coverage

        test_quick_sort.py ............................

        ---------- coverage: platform darwin, python 2.7.12-final-0 ----------
        Name                      Stmts   Miss  Cover   Missing
        -------------------------------------------------------
        quick_sort.py                39     16    59%   50-71


        test_quick_sort.py ............................

        ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
        Name                      Stmts   Miss  Cover   Missing
        -------------------------------------------------------
        quick_sort.py                39     16    59%   50-71
