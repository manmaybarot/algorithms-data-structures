# LIS

# Ref: https://leetcode.com/problems/longest-increasing-subsequence/submissions/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        lis = {}
        lis[0] = 1

        for i in range(1, len(nums)):
            lis[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis.values())
