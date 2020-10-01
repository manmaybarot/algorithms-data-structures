# Given an input string (s) and a pattern (p),
# implement wildcard pattern matching with support
# for '?' and '*'.

# Ref: https://leetcode.com/problems/wildcard-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def helper(s_i, p_i):
            if (s_i, p_i) in memo:
                return memo[(s_i, p_i)]
            if p_i == len(p):
                return s_i == len(s)
            if s_i == len(s):
                for i in range(p_i, len(p)):
                    if p[i] != '*':
                        memo[(s_i, i)] = False
                        return False
                memo[(s_i, i)] = True
                return True

            if s[s_i] == p[p_i] or p[p_i] == '?':
                ans = helper(s_i + 1, p_i + 1)

            elif p[p_i] == '*':
                ans =   helper(s_i, p_i + 1) or helper(s_i + 1, p_i)
            else:
                ans = False

            memo[(s_i, p_i)] = ans
            return ans

        return helper(0, 0)
