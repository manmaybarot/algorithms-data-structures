# Range min query and increment

from math import ceil, log2


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.leaf_nodes = 2**ceil(log2(len(self.arr)))
        self.tree_size = 2 * self.leaf_nodes - 1
        self.tree = [float('inf') for i in range(self.tree_size)]
        self.lazy_tree = [0 for _ in range(self.tree_size)]
        self._build_tree(0, len(self.arr)-1, 0)

    def _build_tree(self, arr_low, arr_high, tree_pos):
        if arr_low == arr_high:
            self.tree[tree_pos] = self.arr[arr_low]
        else:
            arr_mid = (arr_low + arr_high)//2
            left_child_tree_pos = 2*tree_pos + 1
            right_child_tree_pos = 2*tree_pos + 2

            self._build_tree(arr_low, arr_mid, left_child_tree_pos)
            self._build_tree(arr_mid+1, arr_high, right_child_tree_pos)

            self.tree[tree_pos] = min(
                self.tree[left_child_tree_pos],
                self.tree[right_child_tree_pos]
            )

    def get_min_of_range(self, start, end):
        return self._get_min_of_range(start, end, 0, len(self.arr)-1, 0)

    def _get_min_of_range(
        self, range_low, range_high, current_low, current_high, tree_pos
    ):
        if current_low > current_high:
            return float('inf')

        # lazy propogation
        if self.lazy_tree[tree_pos] != 0:
            self.tree[tree_pos] += self.lazy_tree[tree_pos]
            if current_low != current_high:
                self.lazy_tree[2*tree_pos+1] += self.lazy_tree[tree_pos]
                self.lazy_tree[2*tree_pos+2] += self.lazy_tree[tree_pos]
            self.lazy_tree[tree_pos] = 0

        # if complete overlap
        if  current_low >= range_low and current_high <= range_high:
            return self.tree[tree_pos]

        # if no overlap
        if range_low > current_high or range_high < current_low:
            return float('inf')

        # partial overlap
        mid = (current_low + current_high) // 2
        left_child_tree_pos = 2*tree_pos + 1
        right_child_tree_pos = 2*tree_pos + 2

        return min(
            self._get_min_of_range(
                range_low, range_high, current_low, mid, left_child_tree_pos
            ),
            self._get_min_of_range(
                range_low, range_high, mid+1, current_high, right_child_tree_pos
            )
        )

    def increment(self, start, end, delta):
        self._lazy_increment(start, end, delta, 0, len(self.arr)-1, 0)

    def _lazy_increment(
        self,  range_low, range_high, delta, current_low, current_high, tree_pos
    ):
        if current_low > current_high:
            return

        # lazy propogation
        if self.lazy_tree[tree_pos] != 0:
            self.tree[tree_pos] += self.lazy_tree[tree_pos]
            if current_low != current_high:
                self.lazy_tree[2*tree_pos+1] += self.lazy_tree[tree_pos]
                self.lazy_tree[2*tree_pos+2] += self.lazy_tree[tree_pos]
            self.lazy_tree[tree_pos] = 0

        # no overlap
        if current_low > range_high or current_high < range_low:
            return

        # complete overlap
        if current_low >= range_low and current_high <= range_high:
            self.tree[tree_pos] += delta
            if current_low != current_high:
                self.lazy_tree[2*tree_pos + 1] += delta
                self.lazy_tree[2*tree_pos + 2] += delta
            return

        # partial overlap
        mid = (current_low + current_high) // 2
        left_child_tree_pos = 2*tree_pos + 1
        right_child_tree_pos = 2*tree_pos + 2
        self._lazy_increment(
            range_low, range_high, delta, current_low, mid, left_child_tree_pos
        )
        self._lazy_increment(
            range_low, range_high, delta, mid+1, current_high,
            right_child_tree_pos
        )

        self.tree[tree_pos] = min(
            self.tree[left_child_tree_pos], self.tree[right_child_tree_pos]
        )


if __name__ == '__main__':
    arr = [2, 3, -1, 4]
    seg_tree = SegmentTree(arr=arr)
    print(seg_tree.get_min_of_range(0,2))
    seg_tree.increment(0, 2 , 50)
    seg_tree.increment(0, 2 , -50)
    seg_tree.increment(0, 3, 2)
    print(seg_tree.get_min_of_range(0,2))
