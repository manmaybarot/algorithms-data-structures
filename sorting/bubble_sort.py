# Bubble Sort


def bubble_sort(arr):
    j = len(arr) - 1

    while j > 0:
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        j -= 1

    return arr


if __name__ == '__main__':
    arr = [14,3,5,67,85,4,32,4,67,55,66,55]
    print(bubble_sort(arr))
