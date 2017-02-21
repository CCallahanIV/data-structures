"""Test the K-NN algorithm."""
import pytest
import os
import pandas as pd
from math import sqrt


BAD_Ks = [-1, "whoops", 0]
DATA = pd.read_csv(os.path.abspath('src/flowers_data.csv'))

SIMPLE_COLUMNS = ["x", "y", "class"]
SIMPLE_DATA = [[6, 6, 0],
               [5, 5, 0],
               [4, 4, 0],
               [3, 3, 1],
               [2, 2, 1],
               [1, 1, 1],
               [0, 0, 1]]


@pytest.fixture
def simple_knn():
    """Create a default knn with flowers data."""
    data = pd.DataFrame(SIMPLE_DATA, columns=SIMPLE_COLUMNS)
    from knn import KNearestNeighbors
    k = KNearestNeighbors(data)
    return k


def test_initialize_k_nearest_bad_k():
    """Test initializing with bad k value raises error."""
    from knn import KNearestNeighbors
    for test_item in BAD_Ks:
        with pytest.raises(ValueError):
            KNearestNeighbors(DATA, test_item)


def test_initialize_k_nearest_good_k():
    """Test initializing with good k value."""
    from knn import KNearestNeighbors
    k = KNearestNeighbors(DATA, 2)
    assert type(k) is KNearestNeighbors


def test_distance_calc():
    """Test correctness of distance calc funciton."""
    from knn import KNearestNeighbors
    rows = [[2, 2, 1], [0, 0, 1]]
    data = pd.DataFrame(data=rows, columns=['x', 'y', 'class'])
    test_data = KNearestNeighbors(data)
    assert test_data._distance(data.loc[0], data.loc[1]) == sqrt(8)


def test_distance_calc_zero():
    """Test correctness of distance calc funciton when distance is zero."""
    from knn import KNearestNeighbors
    rows = [[2, 2, 1], [2, 2, 1]]
    data = pd.DataFrame(data=rows, columns=['x', 'y', 'class'])
    test_data = KNearestNeighbors(data)
    assert test_data._distance(data.loc[0], data.loc[1]) == 0


def test_classify(simple_knn):
    """Test _classify method returns expected value."""
    knn = simple_knn
    data = pd.DataFrame(data=SIMPLE_DATA, columns=SIMPLE_COLUMNS)
    test_data = [0.5, 0.5]
    distances = []
    for row in data.iterrows():
        distances.append((row[1][-1], knn._distance(row[1], test_data)))
    distances.sort(key=lambda x: x[1])
    assert knn._classify(distances[:5]) == 1


def test_simple_prediction(simple_knn):
    """Test a simple prediction."""
    knn = simple_knn
    test_data = [0.5, 0.5]
    prediction = knn.predict(test_data)
    assert prediction == 1


def test_flowers_integration():
    """Test knn predictions using flowers data."""
    from knn import KNearestNeighbors
    total_data = DATA.drop('target', axis=1)
    calibration_number = len(total_data) // 5
    new_data = total_data.sample(n=calibration_number)
    k = KNearestNeighbors(new_data)
    for row in new_data.iterrows():
        assert k.predict(row[1][:-1]) == row[1][-1]
