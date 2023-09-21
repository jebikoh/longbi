from PIL import Image
from coords import GRID_COORDS, GRID_CELLS, GRID_SIZE
from typing import List
import cv2
import easyocr


# Set to True if GPU is available
USE_GPU = False


def extract_grid(path: str) -> List[List[str]]:
    image = cv2.imread(path)

    x1, y1, x2, y2 = GRID_COORDS
    cropped = image[y1:y2, x1:x2]

    greyscale = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(greyscale, 128, 255, cv2.THRESH_BINARY)

    grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    reader = easyocr.Reader(lang_list=["en"], gpu=USE_GPU)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x1, y1, x2, y2 = GRID_CELLS[(row, col)]
            cell = thresholded[y1:y2, x1:x2]

            # Convert the cell to an image format that EasyOCR can accept
            pil_img = Image.fromarray(cell)
            text_list = reader.readtext(pil_img, detail=0)

            # EasyOCR returns a list, we concatenate it to get the final string
            # and then filter it using the whitelist
            text = "".join(text_list)
            grid[row][col] = "".join(char for char in text if char.isalpha())

    return grid
