#!/usr/bin/python3
"""
Method determining if given data set represents a,
valid UTF-8 encoding
"""


def validUTF8(data):
    """
    method checks if a given binary data sequence
    conforms to the UTF-8 encoding standard
    """
    y_bytes = 0

    x1 = 1 << 7
    x2 = 1 << 6

    for i in data:
        x = 1 << 7
        if y_bytes == 0:
            while x & i:
                y_bytes += 1
                x = x >> 1
            if y_bytes == 0:
                continue
            if y_bytes == 1 or y_bytes > 4:
                return False
        else:
            if not (i & x1 and not (i & x2)):
                return False
        y_bytes -= 1
    return y_bytes == 0
