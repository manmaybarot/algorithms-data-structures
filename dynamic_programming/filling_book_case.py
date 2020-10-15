# Filling Bookcase Shelves

# Ref: https://leetcode.com/problems/filling-bookcase-shelves/

from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [float('inf') for _ in range(len(books)+1)]
        dp[0] = 0

        for i in range(1, len(dp)):
            max_height = 0
            width_left = shelf_width

            for j in range(i-1, -1, -1):
                width_left -= books[j][0]
                max_height = max(max_height, books[j][1])

                if width_left >= 0:
                    dp[i] = min(dp[i], dp[j] + max_height)
                else:
                    break

        return dp[-1]
