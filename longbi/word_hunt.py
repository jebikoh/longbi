from typing import List, Optional, Tuple
from longbi.trie import Trie
import pickle
import os

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


class WordHunt:
    def __init__(self, len_lim: Optional[int] = None):
        self.trie = Trie()
        self.len_lim = len_lim

    def load_text(self, path: str, save: bool = True) -> None:
        with open(path) as f:
            words = f.read().split()
        if self.len_lim:
            for word in words:
                if len(word) <= self.len_lim:
                    self.trie.insert(word)
        else:
            for word in words:
                self.trie.insert(word)

        if save:
            name, _ = os.path.splitext(path)
            with open(f"{name}.pkl", "wb") as f:
                pickle.dump(self.trie, f)

    def load_pkl(self, path: str) -> None:
        with open(path, "rb") as f:
            self.trie = pickle.load(f)

    from typing import List, Tuple

    def solve(self, grid: List[List[str]]) -> List[Tuple[str, List[Tuple[int, int]]]]:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]
        words = set()

        def dfs(row: int, col: int, path: str, node, coords: List[Tuple[int, int]]):
            visited[row][col] = True
            path += grid[row][col]
            coords.append((row, col))
            node = (
                node.get_child(grid[row][col])
                if node.has_child(grid[row][col])
                else None
            )

            if node:
                if node.is_word:
                    words.add((path, tuple(coords)))
                for drow, dcol in DIRECTIONS:
                    nrow, ncol = row + drow, col + dcol
                    if (
                        0 <= nrow < rows
                        and 0 <= ncol < cols
                        and not visited[nrow][ncol]
                    ):
                        dfs(nrow, ncol, path, node, coords)

            visited[row][col] = False
            coords.pop()

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, "", self.trie.root, [])

        return list(words)
