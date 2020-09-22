# Given two strings s1, s2, find the lowest ASCII sum
# of deleted characters to make two strings equal.

# Ref: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/


def minimumDeleteSum(self, s1: str, s2: str) -> int:
    memo = {}

    def get_min_sum(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        cost = 0
        if i == len(s1) and j == len(s2):
            cost = 0
        elif i == len(s1):
            if (i, j + 1) not in memo:
                memo[(i, j + 1)] = get_min_sum(i, j + 1)
            cost = memo[(i, j + 1)] + ord(s2[j])
        elif j == len(s2):
            if (i + 1, j) not in memo:
                memo[(i + 1, j)] = get_min_sum(i + 1, j)
            cost = memo[(i + 1, j)] + ord(s1[i])
        elif s1[i] == s2[j]:
            if (i + 1, j + 1) not in memo:
                memo[(i + 1, j + 1)] = get_min_sum(i + 1, j + 1)
            cost = memo[(i + 1, j + 1)]
        else:
            if (i, j + 1) not in memo:
                memo[(i, j + 1)] = get_min_sum(i, j + 1)
            if (i + 1, j) not in memo:
                memo[(i + 1, j)] = get_min_sum(i + 1, j)

            cost = min(
                memo[(i, j + 1)] + ord(s2[j]),
                memo[(i + 1, j)] + ord(s1[i])
            )

        return cost

    return get_min_sum(0, 0)
