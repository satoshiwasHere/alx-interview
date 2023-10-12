#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
"""
import math


def factors(n):
    """
    factor of n number
    """
    mylist = []
    while n % 2 == 0:
        mylist.append(2)
        n = n / 2
    for y in range(3, int(math.sqrt(n)) + 1, 2):
        while n % y == 0:
            mylist.append(y)
            n = n / y
    if n > 2:
        mylist.append(n)
    return mylist


def minOperations(n):
    """
    calculate the min operations
    """
    if type(n) != int or n < 2:
        return 0
    else:
        numOperations = sum(factors(n))
        return int(numOperations)
