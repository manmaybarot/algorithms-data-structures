# You have d dice, and each die has f faces
# numbered 1, 2, ..., f.

# Return the number of possible ways
# (out of fd total ways) modulo 10^9 + 7
# to roll the dice so the sum of the face
# up numbers equals target.

# Ref: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    modulo = 10**9 + 7
    memo = {}

    def find_ways(d, target):
        if (d, target) in memo:
            return memo[(d, target)]
        if d == 1:
            if target <= f:
                return 1
            else:
                return 0

        result = 0
        for i in range(1, f + 1):
            if target - i > 0:
                result += find_ways(d - 1, target - i)

        memo[(d, target)] = result

        return memo[(d, target)]

    return find_ways(d, target) % modulo
