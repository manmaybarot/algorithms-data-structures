# You are given an integer array nums and you have to return
# a new counts array. The counts array has the property where
# counts[i] is the number of smaller elements to the right of
# nums[i].

class SegmentNode:
    def __init__(self, low, high):
        self.count = 0
        self.low = low
        self.high = high
        self.left = None
        self.right = None


class Solution:
    def _build(self, left, right):
        root = SegmentNode(self.nums[left], self.nums[right])

        if left == right:
            return root
        mid = (left + right) // 2
        root.left = self._build(left, mid)
        root.right = self._build(mid + 1, right)
        return root

    def _update(self, root, val):
        if not root:
            return
        if root.low <= val <= root.high:
            root.count += 1
            self._update(root.left, val)
            self._update(root.right, val)

    def _query(self, root, low, high):
        if low <= root.low and root.high <= high:
            return root.count
        elif high < root.low or root.high < low:
            return 0
        else:
            return self._query(root.left, low, high) + \
                self._query(root.right, low, high)

    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        self.nums = sorted(list(set(nums)))
        root = self._build(0, len(self.nums) - 1) if nums else None

        result = []

        for num in nums:
            result.append(self._query(root, float('-inf'), num - 1))
            self._update(root, num)

        return result[::-1]
