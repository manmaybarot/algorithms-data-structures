# Rotate mat to 90 degree inplace

# Ref: https://leetcode.com/problems/rotate-image/solution/

from typing import List

class Solution:
    def rotate90(self, mat: List[List[int]]) -> None:
            """
            Do not return anything, modify mat in-place instead.
            """
            n = len(mat)

            for row in range(n):
                for col in range(row, n):
                    mat[row][col], mat[col][row] = mat[col][row], mat[row][col]

            for row in mat:
                row.reverse()


    # Follow up:
    # Rotate to 270


    def rotate270(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify mat in-place instead.
        """
        n = len(mat)

        for row in range(n):
            for col in range(row, n):
                mat[row][col], mat[col][row] = mat[col][row], mat[row][col]

        i = 0
        j = n - 1

        while i < j:
            mat[i], mat[j] = mat[j], mat[i]
