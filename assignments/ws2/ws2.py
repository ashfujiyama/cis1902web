"""Worksheet 2"""

# TODO imports

def list_transpose(mat):
    """
    Matrix transpose, using built-in lists.

    Args:
        mat (list): a list of lists representing a square matrix

    Returns:
        list: list representation of the matrix transpose
    """
    return list(map(list, zip(*mat)))


def benchmark_transpose(n_trials=100, mat_size=1000):
    """
    Task 1: performance benchmarking np.transpose() and list_transpose().

    How much faster is the NumPy implementation for the default parameters?

    Args:
        n_trials (int): the number of trials to run, default 100.
        mat_size (int): the (mat_size, mat_size) shape random matrix to create,
            default 1000.

    Returns:
        None
    """
    list_transpose_times = []
    numpy_transpose_times = []

    for trial in range(n_trials):
        # generate a random matrix of shape (mat_size, mat_size)
        rand_mat = np.random.randint(8,
                                     size=(mat_size, mat_size))
        assert rand_mat.shape == (mat_size, mat_size)

        # convert rand_mat to list of lists for our native transpose
        rand_mat_list = rand_mat.tolist()

        # compute how long np.transpose() takes
        np_start_time = time.time()
        np.transpose(rand_mat)
        np_end_time = time.time()
        np_total_time = np_end_time - np_start_time
        numpy_transpose_times.append(np_total_time)

        # TODO time how long the list_transpose() call takes in the same way as above
        list_transpose(rand_mat_list)
        list_transpose_times.append("""TODO""")

    # TODO compute the mean times across the trials
    mean_numpy_time = """TODO"""
    mean_our_time = """TODO"""

    print("Mean numpy matrix transpose time: {} sec".format(mean_numpy_time))
    print("Mean list matrix transpose time: {} sec".format(mean_our_time))


def clip(arr, max_val):
    """
    Task 2: NumPy finger exercises

    Re-assigns elements of arr greater than the given max_val to max_val.

    Args:
        arr (np.ndarray): a 2D ndarray
        max_val (float): the maximum value to clip to

    Returns:
        the modified ndarray arr
    """
    raise NotImplementedError

def time_units(sec_arr):
    """
    Given a 1D array of times in seconds, creates a single matrix of the
    same times in seconds, minutes, hours, and days.

    Args:
        sec_arr (np.ndarray): a 1-dimensional ndarray with (n_times,) shape

    Returns:
        np.ndarray: an array of shape (n_times, 4) with seconds, minutes, hours
            and days

    """
    # use this array for:  sec, min, hr,    day
    TIME_UNITS = np.array([1,   60,  60**2, 24 *(60**2)])

    # For proper broadcasting, do we need sec_arr to be a 1D, or 2D array here?
    raise NotImplementedError


if __name__ == '__main__':
    # set a random seed so that code is reproducible
    np.random.seed(42)

    # Task 1
    benchmark_transpose()

    # Task 2
    A = np.random.randint(0, 8, size=(5,5))
    print(A)
    print(clip(A, 6))

    # Task 3
    # prevent NumPy from printing scientific notation
    np.set_printoptions(suppress=True,
                        formatter={'float_kind':'{:.3f}'.format})
    secs = np.array([60, 120])
    print(time_units(secs))

    # Task 4
    """
    Please place your demo feedback here.
    """
