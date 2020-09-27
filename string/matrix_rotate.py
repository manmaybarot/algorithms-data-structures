# Rotate matrix to 90 degree inplace

# Ref: https://leetcode.com/problems/rotate-image/solution/

from typing import List


def rotate90(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in matrix:
            row.reverse()


# Follow up:
# Rotate to 270


def rotate270(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for row in range(n):
        for col in range(row, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    i = 0
    j = n - 1

    while i < j:
        matrix[i], matrix[j] = matrix[j], matrix[i]
