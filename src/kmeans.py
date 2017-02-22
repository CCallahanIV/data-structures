"""Implementation of the K-Means Classifier."""
import random
from math import sqrt


class KMeansClassifier(object):
    """Implementation of the K-Means Classifier."""

    def __init__(self, max_iter=5, min_step=None):
        """Initialize a K-Means Classifier object."""
        self.max_iter = max_iter
        self.min_step = min_step
        self.fitted = False
        self.centroids = None

    def fit(self, data, k=2):
        """Fit K centroids to given data."""
        if k < 0 or k > len(data):
            raise ValueError("K must be a positive integer less than the length of data.")

        data['group'] = None
        self.centroids = self._random_centroids(data, k)
        iteration = 0
        old_centroids = None

        while not self._should_stop(old_centroids, iteration, k):
            old_centroids = self.centroids
            iteration += 1
            self._classify(data)
            self.centroids = self._assign_centroids(data, k)
        self.fitted = True

    def predict(self, data):
        """Predict the class of given test data after fit."""
        if self.fitted is False:
            raise RuntimeError('Run KMeansClassifier.fit before running predict.')
        self._classify(data)
        return data

    def _calc_distance(self, pt1, pt2):
        """Calculate the distance between two points."""
        dist = 0.0
        print('distance called from: ', pt1, pt2)
        for i in range(len(pt1) - 2):
            print('i:', i, 'pt1:', pt1[i], 'pt2:', pt2[i])
            dist += (pt1[i] - pt2[i])**2
        return sqrt(dist)

    def _classify(self, data):
        """Assign each datapoint t o the nearest centroid."""
        for point in data.iterrows():
            print('point: ', point)
            distances = []
            for cent in self.centroids:
                print('cent', cent)
                distances.append(self._calc_distance(cent, point[1]))
            point[1]["group"] = distances.index(min(distances))

    def _find_mean(self, points):
        """Find the mean coordinates of points."""
        col_means = []
        for column in points:
            col_means.append(points[column].mean())
        return col_means

    def _assign_centroids(self, data, k):
        """Set centroid coordinates to mean of their assigned datapoints."""
        groups = []
        for _ in range(k):
            groups.append(data[data["groups"] == k])
        for idx, group in enumerate(groups):
            self.centroids[idx] = self._find_mean(group)

    def _should_stop(self, old_centroids, centroids, iteration, k):
        """Determine if the fit should stop runnng."""
        if iteration > self.max_iter:
            return True
        centroid_movements = []
        for i in range(k):
            centroid_movements.append(self._calc_distance(old_centroids[i], centroids[i]))
        if self.min_step:
            if max(centroid_movements) < self.min_step:
                return True
        return False

    def _random_centroids(self, data, k):
        """Return randomly generated centroids."""
        k_list = []
        for i in range(k):
            k_list.append([random.uniform(min(data[column]), max(data[column])) for column in range(len(data) - 2)])
        return k_list
