# Methods here are used for initial calculation
# Coordinates are stored as constants for performance
from typing import Dict, Tuple, Any

# Reference Values
GRID_SIZE = 4

WIDTH = 160
GAP = 55

TOP_LEFT_X = 190
TOP_LEFT_Y = 1245

# Constants
GRID_COORDS = (190, 1245, 995, 2050)
GRID_CELLS: Dict[Tuple[int, int], Any] = {
    (0, 0): (0, 0, 160, 160),
    (0, 1): (215, 0, 375, 160),
    (0, 2): (430, 0, 590, 160),
    (0, 3): (645, 0, 805, 160),
    (1, 0): (0, 215, 160, 375),
    (1, 1): (215, 215, 375, 375),
    (1, 2): (430, 215, 590, 375),
    (1, 3): (645, 215, 805, 375),
    (2, 0): (0, 430, 160, 590),
    (2, 1): (215, 430, 375, 590),
    (2, 2): (430, 430, 590, 590),
    (2, 3): (645, 430, 805, 590),
    (3, 0): (0, 645, 160, 805),
    (3, 1): (215, 645, 375, 805),
    (3, 2): (430, 645, 590, 805),
    (3, 3): (645, 645, 805, 805),
}


# Methods
def _calculate_grid_coords():
    return (
        TOP_LEFT_X,
        TOP_LEFT_Y,
        TOP_LEFT_X + (3 * 55) + (4 * 160),
        TOP_LEFT_Y + (3 * 55) + (4 * 160),
    )


def _calculate_grid_cells():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            tl_x = (col * GAP) + (col * WIDTH)
            tl_y = (row * GAP) + (row * WIDTH)
            br_x = tl_x + (WIDTH)
            br_y = tl_y + (WIDTH)
            coord = (tl_x, tl_y, br_x, br_y)
            print(f"({row}, {col}): {coord},")
