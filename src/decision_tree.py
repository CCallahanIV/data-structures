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

    def __init__(self, column=None, split=None, left=None, right=None, data=None):
        self.column = column
        self.data = data
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
        self.fitted = False

    def fit(self, data):
        """Generate conditions for classification of flowers based on training set."""
        self.fitted = True
        depth = 0
        node_args = self._split(data)
        self.root = TreeNode(column=node_args[0], split=node_args[1], data=data)
        node = self.root
        nodes = []
        nodes.append(node)
        depth += 1
        while(depth <= self.max_depth):
            node = nodes.pop()
            node_data = node.data
            node_args = self._split(node_data)
            data_right, data_left, right_type, left_type = self._make_lr_data(data, node_args)
            if self._is_pure(data_right) or depth >= self.max_depth:
                node.right = right_type
            else:
                right_node_args = self._split(data_right)
                node.right = TreeNode(column=right_node_args[0], split=right_node_args[1], data=data_right)
                nodes.append(node.right)
                depth += 1
                if depth >= self.max_depth:
                    self._assign_leaves()
                    return
            if self._is_pure(data_left) or depth >= self.max_depth:
                node.left = left_type
            else:
                left_node_args = self._split(data_left)
                node.left = TreeNode(column=left_node_args[0], split=left_node_args[1], data=data_left)
                nodes.append(node.left)
                depth += 1
                if depth >= self.max_depth:
                    self._assign_leaves()
                    return
            if self._tree_complete():
                return

    def _assign_leaves(self):
        """Assign end leaves to nodes who have children that are None."""
        nodes = []
        nodes.append(self.root)
        while(True):
            node = nodes.pop()
            if type(node.right) == TreeNode:
                nodes.append(node.right)
            if type(node.left) == TreeNode:
                nodes.append(node.left)
            if not node.right:
                node_args = self._split(node.data)
                node.right = self._make_lr_data(node.data, node_args)[2]
            if not node.left:
                node_args = self._split(node.data)
                node.left = self._make_lr_data(node.data, node_args)[3]

    def _make_lr_data(self, data, node_args):
        """Fill data_right and data_left lists depending on column and split."""
        data_right, data_left = [], []
        right_type = {'setosa': 0, 'versicolor': 0}
        left_type = {'setosa': 0, 'versicolor': 0}
        if node_args[0] == 'x':
            for each in data:
                if each[0] > node_args[1]:
                    data_right.append(each)
                    right_type[each[2]] += 1
                else:
                    data_left.append(each)
                    left_type[each[2]] += 1
        elif node_args[0] == 'y':
            for each in data:
                if each[1] > node_args[1]:
                    data_right.append(each)
                    right_type[each[2]] += 1
                else:
                    data_left.append(each)
                    left_type[each[2]] += 1
        if right_type['setosa'] > right_type['versicolor']:
            right_type = 'setosa'
        else:
            right_type = 'versicolor'
        if left_type['setosa'] > left_type['versicolor']:
            left_type = 'setosa'
        else:
            left_type = 'versicolor'
        return data_right, data_left, right_type, left_type

    def _is_pure(self, data):
        """Check to see if the data is pure."""
        setosa = []
        versicolor = []
        for each in data:
            if each[2] == "setosa":
                setosa.append(each)
            else:
                versicolor.append(each)
        if len(setosa) == 0:
            return True
        elif len(versicolor) == 0:
            return True
        return False

        # column_name = self.some_best_column_algorithm()
        # split_pt = self.some_best_split_point_algorithm()
        # if result of splitting produces nodes with at least one value:
        #     node.left = TreeNode(data_idx=node.data_idx where less than split_pt)
        #     node.right = TreeNode(data_idx=node.data_idx where greater than split_pt)
        # elif left has one value or left is purely one label:
        #     end left
        # elif right has one value or right is purely one label:
        #     end right



        # self.root = TreeNode(data_idx=data.index)

        # until max depth or min leaf min_leaf_size
        # split nodes starting at root

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
        min_g = None
        for each in pl_list:
            data_left = []
            data_right = []
            for j in range(len(data)):
                if pl_list[j] < each:
                    data_left.append(data[j])
                else:
                    data_right.append(data[j])
            if len(data_left) == 0 or len(data_right) == 0:
                continue
            g = self._min_func(data, data_left, data_right)
            if min_g is None:
                t = each
                min_g = g
                axis = 'x'
            if g < min_g:
                min_g = g
                t = each
                axis = 'x'
        for each in pw_list:
            data_left = []
            data_right = []
            for j in range(len(data)):
                if pl_list[j] < each:
                    data_left.append(data[j])
                else:
                    data_right.append(data[j])
            if len(data_left) == 0 or len(data_right) == 0:
                continue
            g = self._min_func(data, data_left, data_right)
            if min_g is None:
                t = each
                min_g = g
                axis = 'y'
            if g < min_g:
                min_g = g
                t = each
                axis = 'y'
        return axis, t

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

    def predict(self, data):
        """Return the likely classification for a flower(s) given petal length and petal width."""
        if not self.fitted:
            return "Decision Tree not trained... yet."
        node = self.root
        while(True):
            if node.column == 'x':
                if data[0] < node.split:
                    if type(node.left) == str:
                        return node.left
                    else:
                        node = node.left
                else:
                    if type(node.right) == str:
                        return node.right
                    else:
                        node = node.right
            elif node.column == 'y':
                if data[1] < node.split:
                    if type(node.left) == str:
                        return node.left
                    else:
                        node = node.left
                else:
                    if type(node.right) == str:
                        return node.right
                    else:
                        node = node.right



        # return_list = []
        # for each in data:
        #     if each[0] < 2.5:
        #         return_list.append("setosa")
        #     else:
        #         return_list.append("versicolor")
        # return return_list

###########################################################################

    # def log_scalar(num_array):
    #     top = np.log10(num_array) - min(np.log10(num_array))
    #     bottom = max(np.log10(num_array)) - min(np.log10(num_array))
