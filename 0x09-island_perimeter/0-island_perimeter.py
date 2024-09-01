#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4

                if col < len(grid[row]) - 1 and grid[row][col+1] == 1:
                    perimeter -= 2

                if row < len(grid) - 1 and grid[row+1][col]:
                    perimeter -= 2

    return perimeter
