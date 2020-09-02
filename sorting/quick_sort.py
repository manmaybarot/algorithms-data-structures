# Quick Sort


def quick_sort(p, r):
    global A
    if p < r:
        q = partition(p, r)
        quick_sort(p, q-1)
        quick_sort(q+1, r)


def partition(p, r):
    global A
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    A = [14,3,5,67,85,4,32,4,67,55,66,55]
    quick_sort(0, len(A)-1)
    print(A)
