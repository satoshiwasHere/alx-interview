#!/usr/bin/python3
"""
Rotating 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    Return : null
    """
    for k in range(int(len(matrix) / 2)):
        for j in range(k, (len(matrix) - k - 1)):
            x = (len(matrix) - 1 - j)
            tmp = matrix[i][j]
            matrix[k][j] = matrix[x][k]
            matrix[x][k] = matrix[(len(matrix) - k - 1)][x]
            matrix[(len(matrix) - k - 1)][x] = matrix[j][(len(matrix) - k - 1)]
            matrix[j][(len(matrix) - k - 1)] = tmp
