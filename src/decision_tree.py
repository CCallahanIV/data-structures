
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

    def _calculate_gini(self, data):
        """Calculate gini for a given data_set."""
        pass

    def predict(self, data):
        """Given data, return labels for that data."""
        pass

