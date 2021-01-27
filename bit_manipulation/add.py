# Add two numbers (sum)


def add(x, y):
    if y == 0:
        return x

    partial_sum = x ^ y
    carry = (x ^ y) << 1

    return add(partial_sum, carry)
