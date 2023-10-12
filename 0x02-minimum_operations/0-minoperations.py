#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed to result
"""

def minOperations(n):
    """
    Ealuates the fewest number of operations for a particular result
    """
    if n <= 0:
        return 0

    # initialize lsit to store least operations for each position
    min_op = []
    y = 1
    while n != 1:
        y += 1
        if n % y == 0:
            while n % y == 0:
                n /= y
                min_op.append(y)
    return sum(min_op)
