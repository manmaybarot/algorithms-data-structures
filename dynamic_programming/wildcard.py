# Ref: https://leetcode.com/problems/wildcard-matching/


def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s

    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for col in range(1, len(dp[0])):
        if dp[0][col - 1] and p[col - 1] == '*':
            dp[0][col] = True
        else:
            break


    for r in range(1, len(dp)):
        s_i = r - 1
        for c in range(1, len(dp[0])):
            p_i = c - 1

            if p[p_i] == s[s_i] or p[p_i] == '?':
                dp[r][c] = dp[r - 1][c - 1]
            elif p[p_i] == '*':
                dp[r][c] = dp[r][c - 1] or dp[r - 1][c]
            else:
                dp[r][c] = False

    return dp[-1][-1]
