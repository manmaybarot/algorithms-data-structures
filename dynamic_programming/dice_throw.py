# Calculate total number of ways to achieve given
# sum with n throws of dice having k faces


def calculate_dice_throw_ways(n: int, faces: int, total: int) -> int:
    memo = {}
    def calculate_ways(n, faces, total):
        if (n, total) in memo:
            return memo[(n, total)]
        elif n == 0 and total == 0:
            return 1
        elif n == 0:
            return 0

        result = 0
        for i in range(1, faces + 1):
            result += calculate_ways(n - 1, faces, total - i)

        memo[(n, total)] = result
        return memo[(n, total)]

    return calculate_ways(n, faces, total)


if __name__ == '__main__':
    n = 4
    faces = 6
    total = 15
    print(calculate_dice_throw_ways(n, faces, total))
