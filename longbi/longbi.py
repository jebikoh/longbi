from word_hunt import WordHunt
import time

if __name__ == "__main__":
    wh = WordHunt()
    print("Loading words...")
    start = time.time()
    wh.load_pkl("words.pkl")
    end = time.time()
    print(f"Words loaded in {end-start}s")

    # lwuttihaeldcghao
    test_grid = [
        ["L", "W", "U", "T"],
        ["T", "I", "H", "A"],
        ["E", "L", "D", "C"],
        ["G", "H", "A", "O"],
    ]

    print("Solving grid...")
    start = time.time()
    res = wh.solve(test_grid)
    end = time.time()
    print(res)
    print(f"Solved in {end-start}s")
