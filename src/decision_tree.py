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


class TreeNode(object):
    """An individual node for a decision tree."""

    def __init__(self, column=None, split=None, left=None, right=None):
        self.column = column
        self.split = split
        self.left = left
        self.right = right
        # self.data_idx = data_idx


class DTC(object):
    """
    Decision Tree Class:
    clf.fit(self, data): construct a decision tree based on some incoming data set; returns nothing
    clf.predict(self, data): returns labels for your test data.
    max_depth: limits the maximum number of steps your tree can take down any decision chain.
    min_leaf_size: Limits the minimum number of data points that may exist within a region before ending a decision chain.
    """

    def __init__(self, max_depth=None, min_leaf_size=1):
        """Initialize the DTC object."""
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.root = None

    def fit(self, data):
        """Generate conditions for classification of flowers based on training set."""
        node_args = self._split(data)
        self.root = TreeNode(column=node_args[1], split=node_args[0])

        # self.root = TreeNode(data_idx=data.index)

        # until max depth or min leaf min_leaf_size
        # split nodes starting at root

    def _min_func(self, total_data, data_left, data_right):
        """Docstring."""
        return (len(data_left) / len(total_data)) * self._analyze_purities(data_left) + (len(data_right) / len(total_data)) * self._analyze_purities(data_right)

    def _analyze_purities(self, data):
        """Docstring."""
        setosa = []
        versicolor = []
        for each in data:
            if each[2] == "setosa":
                setosa.append(each)
            else:
                versicolor.append(each)
        return (len(setosa) / len(data)) * (1 - (len(setosa) / len(data))) + (len(versicolor) / len(data)) * (1 - (len(versicolor) / len(data)))

    def _split(self, data):
        """Given some input node containing data, find best column to split on, and assign split point, and child nodes."""

        pl_list = []
        pw_list = []
        for each in data:
            pl_list.append(each[0])
        for each in data:
            pw_list.append(each[1])
        t = None
        axis = None
        data_left = []
        data_right = []
        min_g = None
        for each in pl_list:
            if t is None:
                t = each
                continue
            for j in range(len(data)):
                if pl_list[j] < each:
                    data_left.append(data[j])
                else:
                    data_right.append(data[j])
            if len(data_left) == 0 or len(data_right) == 0:
                continue
            g = self._min_func(data, data_left, data_right)
            if min_g is None:
                min_g = g
            if g < min_g:
                min_g = g
                t = each
                axis = 'x'
            data_left = []
            data_right = []
        for each in pw_list:
            if t is None:
                t = each
                continue
            for j in range(len(data)):
                if pl_list[j] < each:
                    data_left.append(data[j])
                else:
                    data_right.append(data[j])
            if len(data_left) == 0 or len(data_right) == 0:
                continue
            g = self._min_func(data, data_left, data_right)
            if min_g is None:
                min_g = g
            if g < min_g:
                min_g = g
                t = each
                axis = 'y'
            data_left = []
            data_right = []
        return t, axis

        # column_name = self.some_best_column_algorithm()
        # split_pt = self.some_best_split_point_algorithm()
        # if result of splitting produces nodes with at least one value:
        #     node.left = TreeNode(data_idx=node.data_idx where less than split_pt)
        #     node.right = TreeNode(data_idx=node.data_idx where greater than split_pt)
        # elif left has one value or left is purely one label:
        #     end left
        # elif right has one value or right is purely one label:
        #     end right

    def predict(self, data):
        """Return the likely classification for a flower(s) given petal length and petal width."""
        return_list = []
        for each in data:
            if each[0] < 2.5:
                return_list.append("setosa")
            else:
                return_list.append("versicolor")
        return return_list


###########################################################################

        def log_scalar(num_array):
            top = np.log10(num_array) - min(np.log10(num_array))
            bottom = max(np.log10(num_array)) - min(np.log10(num_array))