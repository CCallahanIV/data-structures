import pandas as pd


class TreeNode(object):
    """Define a Node object for use in a decision tree classifier."""

    def __init__(self, data, split_value, split_gini, split_col, left=None, right=None, label=None):
        """Initialize a node object for a decision tree classifier."""
        self.left = left
        self.right = right
        self.data = data
        self.split_value = split_value
        self.split_gini = split_gini
        self.split_col = split_col
        self.label = label

    def _has_children(self):
        """Return True or False if Node has children."""
        if self.right or self.left:
            return True
        return False


class DecisionTree(object):
    """Define a Decision Tree class object."""

    def __init__(self, max_depth, min_leaf_size):
        """Initialize a Decision Tree object."""
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.root = None

    def fit(self, data):
        """Create a tree to fit the data."""
        split_col, split_value, split_gini, split_groups = self._get_split(data)
        new_node = TreeNode(data, split_value, split_gini, split_col)
        self.root = new_node
        self.root.left = self._build_tree(split_groups[0])
        self.root.right = self._build_tree(split_groups[1])

    def _build_tree(self, data, depth_count=1):
        """Given a node, build the tree."""
        split_col, split_value, split_gini, split_groups = self._get_split(data)
        new_node = TreeNode(data, split_value, split_gini, split_col)
        try:
            new_node.label = data[data.columns[-1]].mode()[0]
        except:
            pass
        if self._can_split(split_gini, depth_count, len(data)):
            print("splitting")
            new_node.left = self._build_tree(split_groups[0], depth_count + 1)
            new_node.right = self._build_tree(split_groups[1], depth_count + 1)
        else:
            print("terminating")
            return new_node
        return new_node

    def _can_split(self, gini, depth_count, data_size):
        """Given a gini value, determine whether or not tree can split."""
        if gini == 0.0:
            print("gini zero")
            return False
        elif depth_count >= self.max_depth:
            print("bad depth")
            return False
        elif data_size <= self.min_leaf_size:
            print("bad data size")
            return False
        else:
            return True

    def _depth(self, start=''):
        """Return the integer depth of the BST."""
        def depth_wrapped(start):
            if start is None:
                return 0
            else:
                right_depth = depth_wrapped(start.right)
                left_depth = depth_wrapped(start.left)
                return max(right_depth, left_depth) + 1
        if start is '':
            return depth_wrapped(self.root)
        else:
            return depth_wrapped(start)

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
        if len(data) < 10:
            import pdb; pdb.set_trace()
        classes = data[data.columns[-1]].unique()
        split_col, split_value, split_gini, split_groups = float('inf'), float('inf'), float('inf'), None
        for col in data.columns.values[:-2]:
            for row in data.iterrows():
                groups = self._test_split(col, row[1][col], data)
                gini = self._calculate_gini(groups, classes)
                # import pdb; pdb.set_trace()
                if gini < split_gini and len(groups[0]) > 0 and len(groups[1]) > 0:
                    split_col, split_value, split_gini, split_groups = col, row[1][col], gini, groups
        # print("Col: ", split_col, "s_val: ", split_value, "gini: ", split_gini, "\n groups:", split_groups)
        return split_col, split_value, split_gini, split_groups

    def _test_split(self, col, value, data):
        """Given a dataset, column index, and value, split the dataset."""
        left, right = pd.DataFrame(columns=data.columns), pd.DataFrame(columns=data.columns)
        for row in data.iterrows():
            if row[1][col] < value:
                left = left.append(row[1])
            else:
                right = right.append(row[1])
        return left, right

    def predict(self, data):
        """Given data, return labels for that data."""
        curr_node = self.root
        while curr_node._has_children():
            if data[curr_node.label]:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return curr_node.label

