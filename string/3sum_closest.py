


def threeSumClosest(self, nums: List[int], target: int) -> int:
    diff = float('inf')
    nums.sort()
    for i in range(len(nums)):
        low = i + 1
        high = len(nums)-1
        while low < high:
            current_sum = nums[i] + nums[low] + nums[high]

            if abs(target-current_sum) < abs(diff):
                diff = target-current_sum

            if current_sum < target:
                low += 1
            else:
                high -= 1

        if diff == 0:
            break

    return target - diff
