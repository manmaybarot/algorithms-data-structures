# Calculate total 1's in a binary number of a given number


def calculate_ones(num):
    ones = 0

    while num > 0:
        # ones += num % 2
        ones += num & 1
        num >>= 1

    return ones


if __name__ == '__main__':
    print(calculate_ones(4))
    print(calculate_ones(2))
    print(calculate_ones(19))

# O(Number of bits in X)
# Number of bits in X = log X
# hence, O(log X) where X is number an actual number
