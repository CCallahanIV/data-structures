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
                proportion = len(group[group[group.columns[-1]] == class_value]) / float(size)
                gini += (proportion * (1.0 - proportion))
        return gini

    def _get_split(self, data):
        """Choose a split point with lowest gini index."""
        classes = data[data.columns[-1]].unique()
        split_col, split_value, split_gini, split_groups =\
            float('inf'), float('inf'), float('inf'), None
        for col in data.columns.values[:-2]:
            for i in range(len(data)):
                row = data.iloc[i]
                groups = self._test_split(col, row[col], data)
                gini = self._calculate_gini(groups, classes)
            if gini < split_gini:
                split_col, split_value, split_gini, split_groups =\
                    col, row[col], gini, groups
        return split_col, split_value, split_groups

    def _test_split(self, col, value, data):
        """Given a dataset, column index, and value, split the dataset."""
        left, right = pd.DataFrame(columns=data.columns), pd.DataFrame(columns=data.columns)
        for i in range(len(data)):
            row = data.iloc[i]
            if row[col] < value:
                left = left.append(row)
            else:
                right = right.append(row)
        return left, right

    def predict(self, data):
        """Given data, return labels for that data."""
        pass
