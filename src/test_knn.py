"""Test the K-NN algorithm."""
import pytest
import os
import pandas as pd


BAD_Ks = [-1, "whoops", 0]
DATA = pd.read_csv(os.path.abspath('src/flowers_data.csv'))


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
