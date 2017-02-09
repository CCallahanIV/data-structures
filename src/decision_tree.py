import pandas as pd


class TreeNode(object):
    """Define a Node object for use in a decision tree classifier."""

    def __init__(self, split_value, data_set, label=None, left=None, right=None, parent=None):
        """Initialize a node object for a decision tree classifier."""
        self.left = left
        self.right = right
        self.parent = parent
        self.data_set = data_set
        self.split_value = split_value
        self.label = label


class DecisionTree(object):
    """Define a Decision Tree class object."""

    def __init__(self, max_depth, min_leaf_size):
        """Initialize a Decision Tree object."""
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.root = None
        self.class_values = []

    def fit(self, data):
        """Create a tree to fit the data."""
        pass

    def _calculate_gini(self, groups, class_values):
        """Calculate gini for a given data_set."""
        gini = 0.0
        for class_value in class_values:
            for group in groups:
                size = len(group)
                if size == 0:
                    continue
                proportion = [row[-1] for row in group].count(class_value) / float(size)
                gini += (proportion * (1.0 - proportion))
        return gini

    def _get_split(self, data):
        """Choose a split point with lowest gini index."""
        classes = data["class_names"].unique()
        split_col_index, split_value, split_gini, split_groups =\
            float('inf'), float('inf'), float('inf'), None
        for col_index in range(len(data.columns) - 2):
            for row in data:
                groups = self._test_split(col_index, row[col_index], data)
                gini = self._calculate_gini(groups, classes)
            if gini < split_gini:
                split_col_index, split_value, split_gini, split_groups =\
                    col_index, row[col_index], gini, groups
        return split_col_index, split_value, split_groups

    def _calculate_split(self, data):
        lowest_gini = 1.0
        lowest_row = None
        lowest_col = None
        for row in data:
            for col in data:
                gini = self._calculate_gini(row, col)
                if gini < lowest_gini:
                    lowest_gini = gini
                    lowest_row = row
                    lowest_col = col
        return lowest_row, lowest_col

    def predict(self, data):
        """Given data, return labels for that data."""
        pass
