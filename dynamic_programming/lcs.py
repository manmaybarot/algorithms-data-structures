# Longest Common Subsequence

# Ref: https://leetcode.com/problems/longest-common-subsequence/


def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    dp = {}
    ans = ''

    def find_lcs(t1, t2):
        if t1 < 0 or t2 < 0:
            return 0
        elif text1[t1] == text2[t2]:
            ans = 1
            if (t1-1, t2-1) not in dp:
                dp[(t1-1, t2-1)] = find_lcs(t1-1, t2-1)
            ans += dp[(t1-1, t2-1)]
            return ans
        else:
            if (t1, t2-1) not in dp:
                dp[(t1, t2-1)] = find_lcs(t1, t2-1)
            ans1 = dp[(t1, t2-1)]

            if (t1-1, t2) not in dp:
                dp[(t1-1, t2)] = find_lcs(t1-1, t2)
            ans2 = dp[(t1-1, t2)]

            return max(ans1, ans2)

    return find_lcs(len(text1)-1, len(text2)-1)
