# Merge Sort


def merge_sort(A, p, r):
    if p >= r:
        return A
    mid = (p + r)//2

    A = merge_sort(A, p , mid)
    A = merge_sort(A, mid+1, r)
    A = merge(A, p, mid, r)

    return A


def merge(A, p, q, r):
    left = A[p:q+1]
    right = A[q+1:r+1]

    left.append(float('inf'))
    right.append(float('inf'))

    left_i, right_i = 0, 0

    for i in range(p, r+1):
        if left[left_i] <= right[right_i]:
            A[i] = left[left_i]
            left_i += 1
        else:
            A[i] = right[right_i]
            right_i += 1
    return A


if __name__ == '__main__':
    arr = [14,3,5,67,85,4,32,4,67,55,66,55]
    print(merge_sort(arr, 0, len(arr)-1))
