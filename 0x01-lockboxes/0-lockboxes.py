#!/usr/bin/python3
"""
method that determines if all the boxes can be accesed
"""

def canUnlockAll(boxes):

    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    keys = [0]
    for x in keys:
        for y in boxes[x]:
            if y not in keys and y != x and j < len(boxes) and j != 0:
                keys.append(j)
    if len(keys) == len(boxes):
        return True
    else:
        return False
