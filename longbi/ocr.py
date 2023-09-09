from PIL import Image
from coords import GRID_COORDS, GRID_CELLS, GRID_SIZE
from typing import List
import pytesseract
import cv2
from tesserocr import PyTessBaseAPI

CHAR_WHITELIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TESS_PATH = "/usr/share/tesseract-ocr/4.00/tessdata"


def extract_grid(path: str) -> List[List[str]]:
    image = cv2.imread(path)

    x1, y1, x2, y2 = GRID_COORDS
    cropped = image[y1:y2, x1:x2]

    greyscale = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(greyscale, 128, 255, cv2.THRESH_BINARY)

    grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    with PyTessBaseAPI(path="/usr/share/tesseract-ocr/4.00/tessdata") as api:
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x1, y1, x2, y2 = GRID_CELLS[(row, col)]
                cell = thresholded[y1:y2, x1:x2]
                api.SetVariable("tessedit_char_whitelist", CHAR_WHITELIST)
                api.SetPageSegMode(10)
                api.SetImageBytes(
                    cell.tobytes(),
                    cell.shape[1],
                    cell.shape[0],
                    1,
                    cell.shape[1],
                )
                text = api.GetUTF8Text()
                grid[row][col] = "".join(char for char in text if char.isalpha())
    return grid
