# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements
# of nums except nums[i]

# Ref: https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums

        output_arr = nums[:]
        for i in range(1, len(output_arr)):
            output_arr[i] *= output_arr[i-1]

        i = len(nums)-2

        while i >= 0:
            nums[i] *= nums[i+1]
            i -= 1

        pre = output_arr[0]
        output_arr[0] = nums[1]


        for i in range(1, len(nums)-1):
            temp = pre * nums[i + 1]
            pre = output_arr[i]
            output_arr[i] = temp

        output_arr[-1] = pre

        return output_arr
