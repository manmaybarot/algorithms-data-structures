# Given a positive integer n, find the least number
# of perfect square numbers (for example, 1, 4, 9,
# 16, ...) which sum to n.

# Ref: https://leetcode.com/problems/perfect-squares/

from math import ceil, inf

def numSquares(self, n: int) -> int:
    memo = {}
    m = ceil(n**(1/2))+1

    def helper(total):
        if total in memo:
            return memo[total]
        if total == 0:
            return 0

        result = inf
        for i in range(1, m+1):
            k = i*i
            if k <= total:
                result = min(result, 1 + helper(total - k))
            else:
                break

        memo[total] = result
        return memo[total]

    return helper(n)
