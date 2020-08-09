# Kadane's algorithm

# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.


def maxSubArray(self, nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        if current_sum + num >= num:
            current_sum += num
            max_sum = max(max_sum, current_sum)
        else:
            current_sum = num
            max_sum = max(current_sum, max_sum)

    return max_sum
