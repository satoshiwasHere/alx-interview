#!/usr/bin/python3
"""
function def island_perimeter(grid):
returns the perimeter of the island described in grid:
grid is a list of list of integers
"""


def island_perimeter(grid):
    """A function that outputs the perimeter of an island described by grid"""
    perimeter = 0
    grid_length = len(grid)
    for row in range(grid_length):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                if row - 1 < 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                if column - 1 < 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                if column + 1 >= len(grid[row]) or grid[row][column + 1] == 0:
                    perimeter += 1
                if row + 1 >= grid_length or grid[row + 1][column] == 0:
                    perimeter += 1
    return perimeter
