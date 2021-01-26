# Rotate bits by x bits


def rotate_right(N, x):
    return (N >> x) & (N << (N.bit_lenght() - x))


def rotate_left(N, x):
    return (N << x) & (N >> (N.bit_lenght() - x))
