#!/usr/bin/python3
"""
function 'def pascal_triangle(n)'
"""


def pascal_triangle(n):
    """
    creates a lists of integers
    representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        previous = triangle[-1]
        current = [1]
        for x in range(len(previous) - 1):
            current.append(previous[x] + previous[x + 1])
        current.append(1)
        triangle.append(current)
    return triangle
