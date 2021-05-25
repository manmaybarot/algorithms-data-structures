# Quick Sort


import random

def partition(left, right, pivot_index, nums):
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

    store_index = left
    for i in range(left, right):
        if nums[i] < pivot:
            if i != store_index:
                nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1

    nums[right], nums[store_index] = nums[store_index], nums[right]

    return store_index


def quick_sort(left, right, nums):
    if left < right:
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index, nums)
        quick_sort(left, pivot_index - 1, nums)
        quick_sort(pivot_index + 1, right, nums)


if __name__ == '__main__':
    nums = [14,3,5,67,85,4,32,4,67,55,66,55]
    quick_sort(0, len(nums)-1, nums)
    print(nums)
