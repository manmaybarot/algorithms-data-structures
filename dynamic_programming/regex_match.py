# Ref: https://leetcode.com/problems/regular-expression-matching/


def isMatch(self, s: str, p: str) -> bool:
    '''
        a *
        T F F
    a F T
    a F

    '''
    if not p:
        return not s

    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for c in range(1, len(dp[0])):
        if p[c - 1] == '*':
            dp[0][c] = dp[0][c - 2]

    for r in range(1, len(dp)):
        s_i = r - 1
        for c in range(1, len(dp[0])):
            p_i = c - 1
            currentmatch = p[p_i] in {s[s_i], '.'}

            if currentmatch:
                dp[r][c] = dp[r - 1][c - 1]
            elif p[p_i] == '*':
                # 0 occurence
                dp[r][c] = dp[r][c - 2]
                if p[p_i - 1] in {s[s_i], '.'}:
                    dp[r][c] = dp[r][c] or dp[r - 1][c]
            else:
                dp[r][c] = False

    return dp[-1][-1]
