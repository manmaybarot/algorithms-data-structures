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

