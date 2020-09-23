# Nuber of ways to reach (n)th stair using at most k steps


def ways_to_nth_step(self, n: int, k: int) -> int:
    memo = {}

    def count_steps(n, k):
        if n in memo: return memo[n]
        if n < 0: return 0
        elif n == 0: return 1

        result = 0
        for i in range(1, k + 1):
            if n-i not in memo:
                memo[n-i] = count_steps(n - i, k)
            result += memo[n-i]

        return result

    return count_steps(n, k)
