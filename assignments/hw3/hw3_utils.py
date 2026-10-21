"""
Data generation and plotting utilities we provide for HW 3.
"""
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_breast_cancer

"""Part 1 utils"""


def generate_data(n_samples, random_seed=0):
    """
    Generates sine curve data.

    NOTE: you should NOT modify the implementation of this function

    Args:
        n_samples (int): the number of samples to generate
        random_seed (int): random seed for reproducibility

    Returns:
        X, y (np.ndarray, np.ndarray): the generated x and y values
    """
    np.random.seed(random_seed)
    X = np.random.uniform(0, 2*np.pi, size=n_samples)
    y = np.sin(X) + np.random.normal(0, 0.8, size=n_samples)

    return X, y


"""Part 2 utils"""


def get_breast_cancer_data():
    """
    Returns a subset of the built-in breast cancer data.
    The first feature is the "mean texture" of the tumor cells, while the
    second feature is the "mean concave points" of the tumor cells.

    NOTE: you should NOT modify the implementation of this function

    Args:
        None

    Returns:
        X, y (np.ndarray, np.ndarray): (n_samples, 2) features

    """
    bc_data = load_breast_cancer()

    feat1 = bc_data['feature_names'].tolist().index('mean texture')
    feat2 = bc_data['feature_names'].tolist().index('mean concave points')

    X = bc_data['data'][:, [feat1, feat2]]
    y = bc_data['target']

    return X, y


def plot_decision_boundary(X, y, clf, ax):
    """
    Plots the decision boundary of the given classifier as well as the
    datapoints. The shaded area will be the classifier's predicted decision
    boundaries, while the scatterplot will be colored by the true labels.

    NOTE: you should NOT modify the implementation of this function

    Args:
        X ((n, 2) np.ndarray): The two-feature input matrix
        y ((n,) np.ndarray): The input ys, which are in an n length array.
        ax (matplotlib.axes.Axes): the Axes to plot the decision boundary.

    Returns:
        None, but plots the decision boundary to the given Axes
    """
    # Plot the decision boundary by assigning a color to each point in the mesh
    # Note that x and y here refer to coordinates, not our features and labels
    x_min, x_max = (X[:, 0].min() - 1, X[:, 0].max() + 1)
    y_min, y_max = (X[:, 1].min() - 1, X[:, 1].max() + 1)
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.03),
                         np.arange(y_min, y_max, 0.03))

    # ravel() "flattens" the array in row-major order into 1D
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.pcolormesh(xx, yy, Z, cmap='RdBu', label="test", alpha=0.1,
                  shading='gouraud', edgecolor=None)

    # plot the datapoints themselves
    X_0 = X[y == 0, :]
    X_1 = X[y == 1, :]

    ax.scatter(X_0[:, 0], X_0[:, 1], c='red', edgecolor='black',
               label="malignant", alpha=0.5)
    ax.scatter(X_1[:, 0], X_1[:, 1], c='blue', edgecolor='black',
               label="benign", alpha=0.5)
