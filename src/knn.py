"""Implement a K-Nearest Neighbors aglorithm."""
import pandas as pd
from math import sqrt


class KNearestNeighbors(object):
    """Define a K-Nearest Neighbors object."""

    def __init__(self, data, k=5):
        """Initialize a k nearest neighbors object."""
        if type(k) is not int or k <= 0:
            raise ValueError("Please initalize with positive integer.")
        else:
            self.k = k
        if type(data) is not pd.DataFrame:
            try:
                self.data = pd.DataFrame(data)
            except pd.PandasError:
                pass
        else:
            self.data = data

    def predict(self, test_data, tk=None):
        """Given data, categorize the data by its k nearest neighbors."""
        if tk is None:
            tk = self.k
        if type(test_data) is not pd.DataFrame:
            try:
                test_data = pd.Series(test_data)
            except pd.PandasError:
                raise ValueError("BAD DATA YA TURKEY")
        distances = []
        for row in self.data.iterrows():
            distances.append((row[1][-1], self._distance(row[1], test_data)))
        distances.sort(key=lambda x: x[1])
        my_class = self._classify(distances[:tk])
        if my_class:
            return my_class
        else:
            self.predict(test_data, tk - 1)

    def _classify(self, res_list):
        """Classify an object given a set of data about its classes."""
        classes = {item[0] for item in res_list}
        class_counts = []
        for a_class in classes:
            class_counts.append((a_class, len([item for item in res_list if item[0] == a_class])))
        class_counts.sort(key=lambda x: x[1], reverse=True)
        if class_counts[0][1] == class_counts[1][1]:
            return
        else:
            return class_counts[0][0]

    def _distance(self, row1, row2):
        """Calcute the distance between two rows."""
        dist = 0.0
        for i in range(len(row1) - 1):
            dist += (row1[i] - row2[i]) ** 2
        return sqrt(dist)
