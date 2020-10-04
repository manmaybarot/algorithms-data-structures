# Ref: https://leetcode.com/problems/coin-change/

from math import inf
from typing import List


class Solution:
    def coinChange_memo(self, coins: List[int], amount: int) -> int:
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

    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for current_count in range(coin, amount+1):

                dp[current_count] = min(
                    dp[current_count],          # exclude
                    dp[current_count-coin] + 1  # include
                )

        return dp[-1] if dp[-1] != inf else -1



def test_coin_change():
    coins = [[1,2,5], [2], [1], [3,7,405,436]]
    amounts = [11, 3, 0, 8839]
    expected = [3, -1, 0, 25]
    result = []

    for coins_, amount in zip(coins, amounts):
        result.append(Solution().coinChange_dp(coins_, amount))

    assert result == expected
