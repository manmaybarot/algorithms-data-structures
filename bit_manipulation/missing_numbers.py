# Find 1 and/or 2 missing numbers from an array from 1 to n


def missing_one(arr):
    xor = 0
    for i in range(1, len(arr) + 2):
        xor ^= i

    for j in arr:
        xor ^= j

    return xor


def missing_two(arr):
    n = len(arr) + 2
    total = n * (n + 1) // 2

    for num in arr:
        total -= num

    half = total // 2

    first_missing = 0
    second_missing = 0

    for i in range(1, half + 1):
        first_missing ^= i

    for j in range(half + 1, n + 1):
        second_missing ^= j

    for k in arr:
        if k < half:
            first_missing ^= k
        else:
            second_missing ^= k

    return first_missing, second_missing


if __name__ == '__main__':
    print(missing_one([1, 5, 3, 2]))
    print(missing_two([1, 5, 6, 2]))
