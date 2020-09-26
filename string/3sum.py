# Find all 3 digits whose sum to zero (no dups)

# Ref: https://leetcode.com/problems/3sum/

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    dups = set()
    previous_2sum = {}
    ans = set()

    for first_digit, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(nums[first_digit+1:]):
                val3 = -val1 - val2
                if val3 in previous_2sum and previous_2sum[val3] == first_digit:
                    ans.add(tuple(sorted([val1, val2, val3])))
                previous_2sum[val2] = first_digit

    return ans

if __name__ == '__main__':
    A = [3,0,-2,-1,1,2]
    print(threeSum(A))