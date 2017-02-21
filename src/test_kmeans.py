"""Tests for the K-Means Classifier."""

from math import sqrt
import pandas as pd
import pytest


@pytest.fixture
def kmc():
    """Fixture to return a default KMC."""
    from kmeans import KMeansClassifier
    return KMeansClassifier()


def test_calc_distance(kmc):
    """Test the _calc_distance method of the K Means Classifier."""
    rows = [[2, 2, 1], [0, 0, 1]]
    data = pd.DataFrame(data=rows, columns=['x', 'y', 'class'])
    assert kmc._calc_distance(data.loc[0], data.loc[1]) == sqrt(8)
