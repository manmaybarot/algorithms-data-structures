# Kadane's algorithm

# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.


def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        if current_sum + num >= num:
            current_sum += num
        else:
            current_sum = num
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    A = [
        100, 113, 110, 85, 105, 102, 86,
        63, 81, 101, 94, 106, 101, 79, 94,
        90, 97
    ]

    B = [0]
    for i in range(1, len(A)):
        B.append(A[i] - A[i-1])

    print(maxSubArray(B))
