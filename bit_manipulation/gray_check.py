# Check whether two given numbers are gray numbers of not
# Gray number differs by just one bit


def are_gray(n1, n2):
    xor = n1 ^ n2
    while xor > 0:
        if xor % 2 and xor >> 1 > 0:
            return False
        xor >>= 1

    return True
