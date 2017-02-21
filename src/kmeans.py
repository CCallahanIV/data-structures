"""Implementation of the K-Means Classifier."""


class KMeansClassifier(object):
    """Implementation of the K-Means Classifier."""

    def __init__(self, max_iter=None, min_step=None):
        """Initialize a K-Means Classifier object."""
        self.max_iter = max_iter
        self.min_step = min_step
        self.fitted = False

    def fit(self, data, k=2):
        """Fit K centroids to given data."""
        if k < 0 or k > len(data):
            raise ValueError("K must a positive integer less than the length of data.")

        self.fitted = True
        pass

    def predict(self, data):
        """Predict the class of given test data after fit."""
        pass