# Counting Sort


def counting_sort(A, k):
    C = [0 for i in range(k)]
    B = [0 for i in range(len(A)+1)]

    for i in range(len(A)):
        C[A[i]] += 1
    for j in range(1, len(C)):
        C[j] += C[j-1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1

    return B[1:]


if __name__ == '__main__':
    arr = [14,3,5,67,85,4,32,4,67,55,66,55]
    print(counting_sort(arr, max(arr)+1))
