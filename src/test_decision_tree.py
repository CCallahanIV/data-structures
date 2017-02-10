import pytest
import pandas as pd


DATASET2 = pd.read_csv("src/test_dataset2.csv")
DATASET2_VALUES = [
    (2.771, 'x'),
    (1.728, 'x'),
    (3.678, 'x'),
    (3.961, 'x'),
    (2.999, 'x'),
    (7.497, 'x'),
    (9.002, 'x'),
    (7.444, 'x'),
    (10.124, 'x'),
    (6.642, 'x'),
    (1.784, 'y'),
    (1.168, 'y'),
    (2.812, 'y'),
    (2.619, 'y'),
    (2.209, 'y'),
    (3.162, 'y'),
    (3.339, 'y'),
    (0.476, 'y'),
    (3.234, 'y'),
    (3.319, 'y'),
]

DATASET2_GINI = [
    0.494,
    0.500,
    0.408,
    0.278,
    0.469,
    0.408,
    0.469,
    0.278,
    0.494,
    0.000,
    1.000,
    0.494,
    0.640,
    0.819,
    0.934,
    0.278,
    0.494,
    0.500,
    0.408,
    0.469,
]

# X1 < 2.771 Gini=0.494
# X1 < 1.729 Gini=0.500
# X1 < 3.678 Gini=0.408
# X1 < 3.961 Gini=0.278
# X1 < 2.999 Gini=0.469
# X1 < 7.498 Gini=0.408
# X1 < 9.002 Gini=0.469
# X1 < 7.445 Gini=0.278
# X1 < 10.125 Gini=0.494
# X1 < 6.642 Gini=0.000
# X2 < 1.785 Gini=1.000
# X2 < 1.170 Gini=0.494
# X2 < 2.813 Gini=0.640
# X2 < 2.620 Gini=0.819
# X2 < 2.209 Gini=0.934
# X2 < 3.163 Gini=0.278
# X2 < 3.339 Gini=0.494
# X2 < 0.477 Gini=0.500
# X2 < 3.235 Gini=0.408
# X2 < 3.320 Gini=0.469


def test_test_split():
    """Test _test_split method with test dataset."""
    from decision_tree import DecisionTree
    data = pd.DataFrame([[1.0, 2.0, '1'], [3.0, 4.0, '0'], [5.0, 6.0, '1'], [7.0, 8.0, '0']])
    left = data[data[data.columns[0]] < 3]
    right = data[data[data.columns[0]] >= 3]
    dtree = DecisionTree(1, 1)
    assert dtree._test_split(0, 3, data)[0].equals(left)
    assert dtree._test_split(0, 3, data)[1].equals(right)


def test_calculate_gini():
    """Test calculate gini with know data set."""
    from decision_tree import DecisionTree
    dtree = DecisionTree(1, 1)
    data = pd.DataFrame(DATASET2)
    for i in range(len(DATASET2_VALUES)):
        left, right = dtree._test_split(DATASET2_VALUES[i][1], DATASET2_VALUES[i][0], data)
        assert round(dtree._calculate_gini([left, right], [0.0, 1.0]), 3) == DATASET2_GINI[i]
