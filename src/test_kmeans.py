"""Tests for the K-Means Classifier."""

from math import sqrt
import pandas as pd
import pytest
import numpy as np


@pytest.fixture
def kmc():
    """Fixture to return a default KMC."""
    from kmeans import KMeansClassifier
    return KMeansClassifier()


@pytest.fixture
def some_data():
    """Fixture to return some dummy data."""
    data = np.array([[2, 3], [4, 5], [6, 7], [8, 9], [1, 1], [2, 2], [3, 3], [4, 4]])
    return pd.DataFrame(data=data)


def test_calc_distance_rows(kmc):
    """Test the _calc_distance method of the K Means Classifier."""
    rows = [[2, 2, 1, 0], [0, 0, 1, 0]]
    data = pd.DataFrame(data=rows, columns=['x', 'y', 'class', 'dummy'])
    assert kmc._calc_distance(data.loc[0], data.loc[1]) == sqrt(8)


def test_calc_distance(kmc):
    """Test distance calculator helper method."""
    assert kmc._calc_distance([0, 0, 0, 0], [3, 4, 0, 0]) == 5.0


def test_find_mean(kmc, some_data):
    """Unit test for find mean."""
    data_means = kmc._find_mean(some_data)
    assert data_means == [3.75, 4.25]


def test_should_stop_false_max_iter(kmc):
    """Test that a kmc does not doesnt stop iterating, with only a max iter of 5 set."""
    old_centroids = [[2, 3], [7, 8]]
    new_centroids = [[2, 4], [90, 55]]
    assert not kmc._should_stop(old_centroids, new_centroids, 3, 2)


def test_should_stop_true_max_iter(kmc):
    """Test that a kmc does not doesnt stop iterating, with only a max iter of 5 set."""
    old_centroids = [[2, 3], [7, 8]]
    new_centroids = [[2, 4], [90, 55]]
    assert kmc._should_stop(old_centroids, new_centroids, 6, 2)


def test_classify():
    """Unit test for classifying datapoints."""
    from kmeans import KMeansClassifier
    clusters = KMeansClassifier()
    rows = [[4, 4, 1, 0], [0, 0, 1, 0]]
    data = pd.DataFrame(data=rows, columns=['x', 'y', 'class', 'group'])
    clusters.centroids = None
    clusters.centroids = [[4, 5, 0, 0], [0, 1, 0, 0]]
    # import pdb; pdb.set_trace()
    clusters._classify(data)
    assert True
