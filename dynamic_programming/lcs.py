# Longest Common Subsequence

# Ref: https://leetcode.com/problems/longest-common-subsequence/



def longestCommonSubsequence_memo(self, text1: str, text2: str) -> int:
    memo = {}
    ans = ''

    def find_lcs(t1, t2):
        if t1 < 0 or t2 < 0:
            return 0
        elif text1[t1] == text2[t2]:
            ans = 1
            if (t1-1, t2-1) not in memo:
                memo[(t1-1, t2-1)] = find_lcs(t1-1, t2-1)
            ans += memo[(t1-1, t2-1)]
            return ans
        else:
            if (t1, t2-1) not in memo:
                memo[(t1, t2-1)] = find_lcs(t1, t2-1)
            ans1 = memo[(t1, t2-1)]

            if (t1-1, t2) not in memo:
                memo[(t1-1, t2)] = find_lcs(t1-1, t2)
            ans2 = memo[(t1-1, t2)]

            return max(ans1, ans2)

    return find_lcs(len(text1)-1, len(text2)-1)


def longestCommonSubsequence_dp(text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for row in range(1, len(text1) + 1):
            for col in range(1, len(text2) + 1):
                r = row - 1
                c = col - 1

                if text1[r] == text2[c]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row][col-1], dp[row-1][col])

        return dp[-1][-1]
