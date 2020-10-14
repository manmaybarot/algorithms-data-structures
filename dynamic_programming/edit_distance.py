# Also known as Levenshtien distance

# Ref: https://leetcode.com/problems/edit-distance/submissions/


class Solution:
    def minDistance_memo(self, word1: str, word2: str) -> int:
        memo = {}

        def levenshtien(l1, l2):
            if l1 == -1: return l2 + 1
            elif l2 == -1: return l1 + 1

            if (l1, l2) in memo: return memo[(l1, l2)]

            if word1[l1] == word2[l2]:
                memo[(l1, l2)] = levenshtien(l1-1, l2-1)
            else:
                memo[(l1, l2)] = 1 + min(
                    levenshtien(l1, l2-1),
                    levenshtien(l1-1, l2),
                    levenshtien(l1-1, l2-1)
                )

            return memo[(l1, l2)]

        return levenshtien(len(word1)-1, len(word2)-1)

    def minDistance_dp(self, word1: str, word2: str) -> int:
        table = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(table[0])):
            table[0][i] = i

        for i in range(len(table)):
            table[i][0] = i

        cols = len(word2) + 1
        rows = len(word1) + 1

        for row in range(1, rows):
            for col in range(1, cols):
                w1 = row - 1
                w2 = col - 1
                if word1[w1] == word2[w2]:
                    table[row][col] = table[row-1][col-1]
                else:
                    table[row][col] = 1 + min(table[row-1][col-1], table[row][col-1], table[row-1][col])

        return table[-1][-1]
