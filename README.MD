[![Build Status](https://travis-ci.org/chamberi/data-structures.svg?branch=master)](https://travis-ci.org/chamberi/data-structures)
#Summary

radix_sort: sorts numbers by their 0-9 digits first, putting them in a list from lowest to highest. Next does the same for 10s (10-99), and so forth.

_random_list() returns a list of random numbers from 0 to 300 of random size less than 300. 


## Timeit Information:

                number of runs: 3
                random radix_sort_timed: [0.48798475600779057, 0.4725390509702265, 0.47569359897170216]
                average:  0.4787391353165731

                number of runs: 3
                arranged case radix_sort_timed: [0.48790664895204827, 0.48251010198146105, 0.48216112999944016]
                average:  0.4841926269776498

                number of runs: 3
                reversed case radix_sort_timed: [0.48425215197494254, 0.4971498280065134, 0.4777760480064899]
                average:  0.48639267599598196

## Tests and Coverage

                test_radix.py ..........

                ---------- coverage: platform darwin, python 2.7.12-final-0 ----------
                Name                      Stmts   Miss  Cover   Missing
                -------------------------------------------------------
                radix.py                     43     16    63%   53-74


                test_radix.py ..........

                ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
                Name                      Stmts   Miss  Cover   Missing
                -------------------------------------------------------
                radix.py                     43     16    63%   53-74
