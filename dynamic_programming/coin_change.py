# Ref: https://leetcode.com/problems/coin-change/

from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(n, remaining):
            if (n, remaining) in memo:
                return memo[(n, remaining)]
            if remaining == 0:
                return 1
            elif remaining < 0 or n < 0:
                return inf

            exclude = helper(n-1, remaining)
            include = 1 + helper(n, remaining-coins[n])

            memo[(n, remaining)] = min(include, exclude)
            return memo[(n, remaining)]

        ans = helper(len(coins)-1, amount) - 1
        return ans if ans != inf else -1
