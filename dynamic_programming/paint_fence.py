# There is a fence with n posts, each post can be painted with
# one of the k colors.

# You have to paint all the posts such that no more than two
# adjacent fence posts have the same color.

# Return the total number of ways you can paint the fence.

# Explanation: https://www.youtube.com/watch?v=deh7UpSRaEY&t=56s

def numWays(self, n: int, k: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return k

    same = k
    diff = k * (k - 1)

    for _ in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)

    return same + diff
