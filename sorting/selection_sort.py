# Selection Sort


def selection_sort(arr):
    j = len(arr) - 1

    while j > 0:
        current = 0
        for i in range(1, j+1):
            if arr[i] > arr[current]:
                current = i

        arr[j], arr[current] = arr[current], arr[j]
        j -= 1

    return arr


if __name__ == '__main__':
    arr = [14,3,5,67,85,4,32,4,67,55,66,55]
    print(selection_sort(arr))
