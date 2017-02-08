
class DecisionTree(object):
    """Define a Decision Tree class object."""

    def __init__(self, max_depth, min_leaf_size):
        """Initialize a Decision Tree object."""
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.root = None

    def fit(self, data):
        """Create a tree to fit the data."""
        pass

    def predict(self, data):
        """Given data, return labels for that data."""
        pass
