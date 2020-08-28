# Insertion Sort


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    arr = [14,3,5,67,85,4,32,4,67,55,66,55]
    print(insertion_sort(arr))
