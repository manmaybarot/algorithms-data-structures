# Find a sub-array of a given array whose sum is the greatest
# among all other sub-arrays.
# i.e: Find the best time to buy and sell stock to maximize profit.


def find_max_crossing_sub_array(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    sum = 0
    for j in range(mid+1, high+1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_sub_array(A, low, high):
    if low == high:
        return low, high, A[low]

    mid = (low + high)//2

    left_low, left_high, left_sum = find_max_sub_array(A, low, mid)
    right_low, right_high, right_sum = find_max_sub_array(A, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_sub_array(
        A, low, mid, high
    )

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    A = [
        100, 113, 110, 85, 105, 102, 86,
        63, 81, 101, 94, 106, 101, 79, 94,
        90, 97
    ]

    B = [0]
    for i in range(1, len(A)):
        B.append(A[i] - A[i-1])

    print(find_max_sub_array(B, 0, len(B)-1))
