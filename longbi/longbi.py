from word_hunt import WordHunt
from ocr import extract_grid
import time

if __name__ == "__main__":
    wh = WordHunt()
    print("==========LONGBI============")
    print("Loading words...")
    start = time.time()
    wh.load_pkl("words.pkl")
    end = time.time()
    print(f"Words loaded in {end-start}s")
    print("============================")

    # grid = [
    #     ["L", "W", "U", "T"],
    #     ["T", "I", "H", "A"],
    #     ["E", "L", "D", "C"],
    #     ["G", "H", "A", "O"],
    # ]

    print(f"Extracting grid...")
    start = time.time()
    grid = extract_grid("test/grid.png")
    end = time.time()
    print(grid)
    print(f"Extracted grid in {end-start}s")
    print("============================")

    print("Solving grid...")
    start = time.time()
    res = wh.solve(grid)
    end = time.time()
    print(res)
    print(f"Solved in {end-start}s")
