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
        pl_list = []
        pw_list = []
        for each in data:
            pl_list.append(each[0])
        for each in data:
            pw_list.append(each[1])
        t = None
        data_left = []
        data_right = []
        min_g = None
        # import pdb; pdb.set_trace()
        for i in range(int(max(pl_list))):
            if t is None:
                t = i
                continue
            for j in range(len(data)):
                if pl_list[j] < i:
                    data_left.append(data[j])
                else:
                    data_right.append(data[j])
            if len(data_left) == 0 or len(data_right) == 0:
                continue
            g = self.G(data, data_left, data_right)
            if min_g is None:
                min_g = g
            if g < min_g:
                min_g = g
                t = i
            data_left = []
            data_right = []
        for i in range(int(max(pw_list))):
            if t is None:
                t = i
                continue
            for j in range(len(data)):
                if pl_list[j] < i:
                    data_left.append(data[j])
                else:
                    data_right.append(data[j])
            if len(data_left) == 0 or len(data_right) == 0:
                continue
            g = self.G(data, data_left, data_right)
            if min_g is None:
                min_g = g
            if g < min_g:
                min_g = g
                t = i
            data_left = []
            data_right = []
        return t

    def G(self, total_data, data_left, data_right):
        """Docstring."""
        return (len(data_left) / len(total_data)) * self.H(data_left) + (len(data_right) / len(total_data)) * self.H(data_right)

    def H(self, data):
        """Docstring."""
        setosa = []
        versicolor = []
        for each in data:
            if each[2] == "setosa":
                setosa.append(each)
            else:
                versicolor.append(each)
        return (len(setosa) / len(data)) * (1 - (len(setosa) / len(data))) + (len(versicolor) / len(data)) * (1 - (len(versicolor) / len(data)))

    def predict(self, data):
        """Docstring."""
        return_list = []
        for each in data:
            if each[0] < 2.5:
                return_list.append("setosa")
            else:
                return_list.append("versicolor")
        return return_list
