# Ref: https://leetcode.com/problems/search-in-rotated-sorted-array/


from typing import List


def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return -1
    if n == 1:
        return 0 if nums[0] == target else -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1
