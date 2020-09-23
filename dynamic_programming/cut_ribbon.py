# Polycarpus has a ribbon, its length is n.
# He wants to cut the ribbon in a way that
# fulfils the following two conditions:

# After the cutting each ribbon piece should have
# length a, b or c.
# After the cutting the number of ribbon pieces
# should be maximum.

# Ref: https://codeforces.com/problemset/problem/189/A


def get_max_ribbon_pieces(n: int, a: int, b: int, c: int) -> int:
    memo = {}

    def get_max(n):
        if n in memo: return memo[n]
        elif n <= 0: return 0

        if n - a not in memo:
            memo[n - a] = get_max(n - a)
        if n - b not in memo:
            memo[n - b] = get_max(n - b)
        if n - c not in memo:
            memo[n - c] = get_max(n - c)

        return 1 + max(memo[n - a], memo[n - b], memo[n - c])
