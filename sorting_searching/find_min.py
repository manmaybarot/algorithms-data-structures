# find min in sorted rotated array, no duplicates
# Ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


from typing import List


def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + ((right - left) // 2)

        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            return nums[mid]

    return nums[left]




# find min in sorted rotated array, with duplicates
# Ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/



def findMin(self, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right -= 1

    return nums[left]
