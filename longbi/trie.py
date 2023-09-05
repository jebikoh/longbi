from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

    @staticmethod
    def _index(c: str) -> int:
        return ord(c) - ord("A")

    def has_child(self, c: str) -> bool:
        return self.children[self._index(c)] != None

    def get_child(self, c: str) -> "TrieNode":
        child = self.children[self._index(c)]
        if child is None:
            raise ValueError(f"No child node exists for character {c}")
        return child

    def set_child(self, c: str, node) -> None:
        self.children[self._index(c)] = node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.has_child(c):
                node.set_child(c, TrieNode())
            node = node.get_child(c)
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.has_child(c):
                return False
            node = node.get_child(c)
        return node.is_word
