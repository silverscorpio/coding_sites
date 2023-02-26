# HackerRank problem - Dominant cells in a grid
# a dominant cell is one which has a strictly greater value than its neighbours (command side or corner)

from typing import List, Dict


def get_neighbours(grid_rows: int, grid_cols: int) -> Dict:
    neighbours = {}
    for row in range(grid_rows):
        for col in range(grid_cols):
            pairs = []
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if (i, j) != (row, col) and ((-1 < i < grid_rows) and (-1 < j < grid_cols)):
                        pairs.append((i, j))
            neighbours[(row, col)] = pairs

    return neighbours


def dominant_cells(grid: List[List]) -> int:
    num_dominant_cells = 0
    grid_neighbours = get_neighbours(len(grid), len(grid[0]))
    for cell, cell_neighbours in grid_neighbours.items():
        dominance_check = [grid[cell[0]][cell[1]] > grid[i[0]][i[1]] for i in cell_neighbours]
        if all(dominance_check):
            num_dominant_cells += 1
    return num_dominant_cells


print(f"Number of Dominant Cells: {dominant_cells([[1, 2, 7], [4, 5, 6], [8, 8, 9]])}")


# ans = get_neighbours([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# ans = get_neighbours(3, 3)
# # ans = get_neighbours([[0, 1], [2, 3]])
# for key in ans:
#     print(f"{key}: {ans[key]}, ------, 'num_neighbours': {len(ans[key])}")
# for i, j in ans.items():
#     for p in j:
#         print(p)