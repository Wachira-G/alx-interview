#!/usr/bin/python3


def island_perimeter(grid):
    """Calculate the perimeter of an island represend with an array."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Check if the cell represents land
                perimeter += 4  # Add 4 sides initially
                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 if left neighbor is land
                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if top neighbor is land

    return perimeter
