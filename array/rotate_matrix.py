# Rotate Matrix clockwise 90, 180, 270


def rotate_90(matrix):
    print('rotate_90')
    print_matrix(matrix)

    # transpose
    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    print_matrix(matrix)

    # flip it
    for row in matrix:
        row.reverse()

    print_matrix(matrix)


def rotate_270(matrix):
    print('rotate_270')
    print_matrix(matrix)

    # flip it
    for row in matrix:
        row.reverse()

    print_matrix(matrix)

    # transpose
    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    print_matrix(matrix)


def rotate_180(matrix):
    print('rotate_180')
    top = 0
    bottom = len(matrix) - 1

    print_matrix(matrix)

    while top < bottom:
        matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
        top += 1
        bottom -= 1

    # flip it
    for row in matrix:
        row.reverse()

    print_matrix(matrix)


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print('-----------')


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_90(matrix)

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_270(matrix)

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_180(matrix)
