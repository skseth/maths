import numpy as np


def RowSwap(A: np.ndarray, g: int, h: int):
    # =============================================================================
    #     A is a NumPy array.  RowSwap will return duplicate array with rows
    #     g and h swapped.
    # =============================================================================
    n = A.shape[1]  # n is number of columns in A
    B = np.copy(A)
    for j in range(n):
        temp = B[g][j]
        B[g][j] = B[h][j]
        B[h][j] = temp

    return B


def RowScale(A: np.ndarray, g: int, scale: float):
    # =============================================================================
    #     A is a NumPy array.  RowScale will return duplicate array with the
    #     entries of row g multiplied by scale.
    # =============================================================================
    n = A.shape[1]  # n is number of columns in A

    B = np.copy(A).astype(np.float64)

    for j in range(n):
        B[g][j] *= scale

    return B


def RowAdd(A: np.ndarray, g: int, h: int, scale: float):
    # =============================================================================
    #     A is a numpy array.  RowAdd will return duplicate array with row
    #     h modifed.  The new values will be the old values of row g added to
    #     the values of row h, multiplied by scale.
    # =============================================================================
    n = A.shape[1]  # n is number of columns in A

    B = np.copy(A).astype(np.float64)

    for j in range(n):
        B[h][j] += B[g][j]*scale

    return B
