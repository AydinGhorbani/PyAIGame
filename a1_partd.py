# copy over your a1_partd.py file here
#    Main Author(s): Aydin Ghorbani
#    Main Reviewer(s): Bahar NikfalAzar

from a1_partc import Queue 

def get_overflow_list(grid):
    rows = len(grid) 
    cols = len(grid[0])  
    overflow_cells = []  

    # Iterate through each row and column in the grid
    for i in range(rows):
        for j in range(cols):  
            target = 2  # Start with a base of 2 neighbor cell

            # Check for top and bottom neighbors
            if i > 0:  # Has a top neighbor
                if i < rows - 1:  # Has a bottom neighbor
                    target = target + 1  

            # Check for left and right neighbors
            if j > 0:  # Has a left neighbor
                if j < cols - 1:  # Has a right neighbor
                    target = target + 1  

            # Check if the Target's value meets the overflow criteria
            if abs(grid[i][j]) >= target:
                # If so, append its val to the overflow list
                overflow_cells.append((i, j)) 

    # Check if any overflow cells were found
    return None if len(overflow_cells) == 0 else overflow_cells


def overflow(grid, queue):
    # Retrieve overflow cells using the optimized helper function
    overflow_locations = get_overflow_list(grid)

    # Initialize counters for positive and negative cell values
    goodCell, badCell = 0, 0

    # Iterate over the grid to count positive and negative cell values
    for row in grid:
        for cell_value in row:
            goodCell += cell_value > 0
            badCell += cell_value < 0

    # Check if all cells are of the same sign
    unionCell = goodCell == 0 or badCell == 0

    # Return early if no overflow locations or all cells have the same sign
    if overflow_locations is None or unionCell:
        return 0

    # Prepare to adjust neighboring cells
    cells_to_adjust = []
    for row_idx, col_idx in overflow_locations:
        # Identify the sign of the current overflow cell
        cell_sign = -1 if grid[row_idx][col_idx] < 0 else 1
        grid[row_idx][col_idx] = 0  # Reset the current overflow cell to 0

        # Collect coordinates and signs for neighboring cells
        cells_to_adjust.extend([
            (row_idx - 1, col_idx, cell_sign), 
            (row_idx + 1, col_idx, cell_sign), 
            (row_idx, col_idx - 1, cell_sign), 
            (row_idx, col_idx + 1, cell_sign)
        ])

    # Process adjustments for neighboring cells
    for row_idx, col_idx, cell_sign in cells_to_adjust:
        if 0 <= row_idx < len(grid) and 0 <= col_idx < len(grid[0]):
            grid[row_idx][col_idx] = cell_sign * (abs(grid[row_idx][col_idx]) + 1)

    # Enqueue the current grid state
    queue.enqueue([row.copy() for row in grid])

    # Recursively call the function and increment the counter
    return 1 + overflow(grid, queue)
