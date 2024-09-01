#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0
    for row in range(len(grid)-1):
        for col in range(len(grid[row])-1):
            if grid[row][col] == 1:
                perimeter += 1
                if grid[row][col+1] == 1 and grid[row-1][col] == 1:
                    perimeter += 1
    return perimeter * 2
