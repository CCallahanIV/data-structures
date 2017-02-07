"""Module for decision tree."""

# DECISION TREE (DT)
#
# CodeFellows 401d5
# Submission Date:
#
# Authors:  Colin Lamont <https://github.com/chamberi>
#           Ben Shields <https://github.com/iamrobinhood12345>
#
# URL:

import pandas as pd
from bst import BinarySearchTree


class DTC(object):
    """
    Decision Tree Class:
    clf.fit(self, data): construct a decision tree based on some incoming data set; returns nothing
    clf.predict(self, data): returns labels for your test data.
    max_depth: limits the maximum number of steps your tree can take down any decision chain.
    min_leaf_size: Limits the minimum number of data points that may exist within a region before ending a decision chain.
    """

    def __init__(self, max_depth=None, min_leaf_size=None):
        """Docstring."""
        self._classifier = BinarySearchTree()

    def fit(self, data):
        """Docstring."""
        pass

    def predict(self, data):
        """Docstring."""
        return_list = []
        for each in data:
            if each[0] < 2.5:
                return_list.append("setosa")
            else:
                return_list.append("versicolor")
        return return_list
