# Word search 2
# Ref: https://leetcode.com/problems/word-search-ii/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False

    def insert(self, word):
        trie = self
        for w in word:
            if w not in trie.children:
                trie.children[w] = TrieNode()
            trie = trie.children[w]
        trie.ends = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        visited = set()
        matched_words = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                char = board[r][c]
                if char in trie.children:
                    self.dfs_backtrack(r, c, trie, '', board, visited, matched_words)

        return list(matched_words)

    def dfs_backtrack(self,r, c, trie, word, board, visited, matched_words):
        char = board[r][c]

        if char in trie.children:
            word += char
            trie = trie.children[char]

            if trie.ends:
                matched_words.add(word)

            visited.add((r, c))

            for row, col in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                if 0 <= row < len(board) and 0 <= col < len(board[0]):
                    if (row, col) not in visited:
                        self.dfs_backtrack(
                            row, col, trie, word, board, visited, matched_words,
                        )

            visited.remove((r, c))
