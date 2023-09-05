from PIL import Image
from coords import GRID_COORDS, GRID_CELLS, GRID_SIZE
from typing import List
import pytesseract


def extract_grid(path: str) -> List[List[str]]:
    image = Image.open(path)
    coordinates = GRID_COORDS
    cropped = image.crop(coordinates)

    greyscale = cropped.convert("L")

    threshold = 128
    thresholded = greyscale.point(lambda p: 255 if p > threshold else 0)

    grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell = thresholded.crop(GRID_CELLS[(row, col)])  # type: ignore
            text = pytesseract.image_to_string(cell, config="--psm 10")
            grid[row][col] = "".join(char for char in text if char.isalpha())
    return grid
