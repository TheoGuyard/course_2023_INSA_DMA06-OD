import numpy as np
import pulp


def solve_mtz(M):
    """
    Solves the TSP instance encoded in the adjacency matrix M by solving its
    Miller–Tucker–Zemlin formulation.

    Arguments
    ---------
    M : np.ndarray
        The adjacency matrix.

    Returns
    -------
    cost : int or float
        The solution tour cost.
    """
    return -1
