from PIL import Image
from coords import GRID_COORDS, GRID_CELLS, GRID_SIZE
from typing import List
import cv2
import pytesseract

CHAR_WHITELIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def extract_grid(path: str) -> List[List[str]]:
    image = cv2.imread(path)

    x1, y1, x2, y2 = GRID_COORDS
    cropped = image[y1:y2, x1:x2]

    greyscale = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(greyscale, 128, 255, cv2.THRESH_BINARY)

    config = f"--psm 10 -c tessedit_char_whitelist={CHAR_WHITELIST}"

    grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x1, y1, x2, y2 = GRID_CELLS[(row, col)]
            cell = thresholded[y1:y2, x1:x2]
            pil_image = Image.fromarray(cell)
            text = pytesseract.image_to_string(pil_image, config=config)
            grid[row][col] = "".join(char for char in text if char.isalpha())

    return grid
