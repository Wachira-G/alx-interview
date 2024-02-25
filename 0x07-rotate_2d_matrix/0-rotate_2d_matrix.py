#!/usr/bin/python3

"""Has the 2d matrix function."""


def rotate_2d_matrix(matrix):
    """Rotate an nxn matrix 90 degrees clockwise"""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
