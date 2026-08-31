"""
HW 3: Machine Learning

Name:

PennKey:

Number of hours spent on homework:

Collaboration is NOT permitted.

In the functions below the "NotImplementedError" exception is raised, for
you to fill in. The interpreter will not consider the empty code blocks
as syntax errors, but the "NotImplementedError" will be raised if you
call the function. You will replace these raised exceptions with your
code completing the function as described in the docstrings.
"""
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier

from hw4_utils import generate_data, get_breast_cancer_data, \
                      plot_decision_boundary

"""Part 1"""


def make_poly_features(X, max_deg):
    """
    Augments X with additional degrees.

    NOTE: the output is always a 2-dimensional array, even when max_deg is 1!

    Args:
        X (np.ndarray): a 1-dimensional ndarray with (n_samples,) shape
        max_deg (int): the maximum polynomial degree to generate, >= 1

    Returns
        np.ndarray: (n_samples, max_deg) shape ndarray with polynomial features
        per column
    """
    raise NotImplementedError


def make_train_test_idxs(X, train_pct=0.5):
    """
    Returns a tuple of randomized indices for a *mutually exclusive* train and
    test split. This can then be used to select data.

    Please do *not* use the built-in sklearn function to implement this.

    Hint: you can use np.random.shuffle() or np.random.permutation() for
    randomization

    Args:
        X (np.ndarray): a (n_samples, n_features) or (n_samples, ) shape ndarray
        train_pct (float): a ratio between 0 and 1 that determines the number
                           of training samples.

    Returns:
        (np.ndarray, np.ndarray): a tuple of 1D ndarrays that correspond to
                                  row indices for train and test splits.
    """
    raise NotImplementedError


def fit_poly_regression(X, y, deg):
    """
    First transforms X into polynomials of max degree deg, then fits and
    returns a trained LinearRegression model.

    NOTE: make_poly_features() needs to be implemented

    When initializing your LinearRegression model, leave all parameters at 
    their defaults.

    Args:
        X (np.ndarray): a (n_samples, ) shaped array
        y (np.ndarray): a (n_samples, ) shaped array of outcomes
        deg (int): the max degree polynomial to transform

    Returns:
        LinearRegression: the trained linear regression model
    """
    raise NotImplementedError


def plot_curves(X, y):
    """
    Fits three models with different polynomial degrees (1, 5, 12) to the given
    data, and plots their predictions in 3 different subplots.

    NOTE: fit_poly_regression() and make_train_test_idxs() need to be
    implemented.

    Args:
        X (nd.array): a (n_samples, ) shaped array of features
        y (nd.array): a (n_samples, ) shaped array of outcomes

    Returns:
        None, but writes plot to poly_curves.png file
    """
    # use plot_x as the x argument for your plots
    plot_X = np.linspace(0, 2*np.pi, 100)

    # the three columns correspond to 1, 5, 12 degree polynomials
    degrees = [1, 5, 12]
    predictions = np.zeros((len(plot_X), len(degrees)))

    train_idx, _ = make_train_test_idxs(X)

    for i, degree in enumerate(degrees):
        reg = fit_poly_regression(X[train_idx], y[train_idx], degree)
        predictions[:, i] = reg.predict(make_poly_features(plot_X, degree))

    """
    TODO: Create a plot with 3 subplots in a single row and labels for each
    degree polynomial, using plot_X and predictions you defined above.

    Suggestions:
        - pass figsize=(18,6) as a keyword parameter to plt.subplots() for a
          wider figure
        - plot the original data (X, y) using ax.scatter()
        - use fig.legend() and fig.suptitle() as additional artists
    """
    raise NotImplementedError

    fig.savefig("poly_curves.png")


def run_experiment(n_trials=100, n_samples=200, max_deg=12, train_pct=0.5):
    """
    Runs an experiment, training n_trials models for each polynomial degree, up
    to max_deg, and returns both the test and train scores across the trials.

    NOTE: make_poly_features(), fit_poly_regression() and
    make_train_test_idxs() need to be implemented.

    Args:
        n_trials (int): the number of trials to run for each sample
        n_samples (int): the number of samples to generate per trial
        max_deg (int): the maximum polynomial to generate
        train_pct (float): the percentage of the samples to use for training

    Returns:
        (np.ndarray, np.ndarray):
            The train_scores and test_scores, both shape (n_trials, max_deg).
            The ith column corresponds to the scores for the i+1 degree
            polynomial.
    """
    train_scores = np.zeros((n_trials, max_deg))
    test_scores = np.zeros((n_trials, max_deg))

    for trial in range(n_trials):
        X, y = generate_data(n_samples, random_seed=trial)
        train_idx, test_idx = make_train_test_idxs(X)

        for deg in range(max_deg):
            # +1 offset for polynomial
            reg = fit_poly_regression(X[train_idx], y[train_idx], deg+1)

            poly_X = make_poly_features(X, deg+1)
            train_score = reg.score(poly_X[train_idx], y[train_idx])
            test_score = reg.score(poly_X[test_idx], y[test_idx])

            train_scores[trial, deg] = train_score
            test_scores[trial, deg] = test_score

    return train_scores, test_scores


def plot_scores(train_scores, test_scores, max_deg=12):
    """
    Plots the mean train and test R2 scores for each polynomial degree given.

    Suggestions:
        - use ax.set_xticks() to change the x-axis tick frequency

    Args:
        train_scores (np.ndarray): a (n_trials, max_deg) shaped array with
                                   training R2 scores
        test_scores (np.ndarray): a (n_trials, max_deg) shaped array with
                                  testing R2 scores

    Returns:
        None, but writes plot to poly_scores.png file
    """
    raise NotImplementedError

    fig.savefig("poly_scores.png")


"""Part 2"""


def standardize(X):
    """
    Copies then standardizes the data X so that each feature (column)
    has zero mean and standard deviation one.

    If X were one dimensional, this could be accomplished by:
    (X - np.mean(X)) / np.std(X).

    Args:
        X (np.ndarray): (n_samples, n_features) shape array

    Returns:
        np.ndarray: a (n_samples, n_features) shape array, standardized
    """
    standard_X = X.copy()

    raise NotImplementedError

    return standard_X


def fit_knn(X, y, k):
    """
    Fits and returns a k-nearest neighbors classifier on the given data.

    Set k as the number of neighbors, leave all other parameters for
    KNeighborsClassifier at their defaults.

    Args:
        X (np.ndarray): (n_samples, n_features) shape array
        y (np.ndarray): (n_samples,) shape array of outcomes
        k (int): the number of neighbors to use for the classifier

    Returns:
        KNeighborsClassifier: the trained knn classifier
    """
    raise NotImplementedError


def knn_decision_boundaries():
    """
    Plots the k-NN decision boundaries for our breast cancer data.

    NOTE: make_train_test_idxs(), standardize(), and fit_knn() need to be 
    implemented.

    Args:
        None

    Returns:
        None, but creates knn_decision_boundaries.png file
    """

    # get train and test splits, as well as standardized data
    X, y = get_breast_cancer_data()
    std_X = standardize(X)
    train_idx, test_idx = make_train_test_idxs(X, train_pct=0.5)

    fig, axes = plt.subplots(2, 3, figsize=(20, 10))

    ks = [1, 10, 100]
    for row, data in enumerate([X, std_X]):
        for col, k in enumerate(ks):
            cur_ax = axes[row, col]
            knn = fit_knn(data[train_idx], y[train_idx], k)
            plot_decision_boundary(data[test_idx], y[test_idx], knn, cur_ax)
            cur_ax.set_title("k={}, test accuracy: {:.2f}".format(k,
                             knn.score(data[test_idx], y[test_idx])))

    axes[0, 0].set_ylabel("Non-standardized features")
    axes[1, 0].set_ylabel("Standardized features")
    axes[0, 2].legend()
    fig.savefig("knn_decision_boundaries.png")


if __name__ == "__main__":
    """
    TODO: run this code after implementing plot_curves() to generate the plot

    n_samples = 300
    X, y = generate_data(n_samples)
    plot_curves(X,y)
    """
    pass

    """
    TODO: run this code after implementing plot_scores() to generate the plot

    train_scores, test_scores = run_experiment()
    plot_scores(train_scores, test_scores)
    """

    """
    TODO: run this code after implementing standardize() and fit_knn() to
    generate the decision boundaries plot.

    NOTE: this may take ~15-20 seconds to complete.

    knn_decision_boundaries()
    """

    """
    TODO fill out your responses to the discussion questions here.

    Part 1
    1.

    2.

    Part 2
    1.

    2.
    """