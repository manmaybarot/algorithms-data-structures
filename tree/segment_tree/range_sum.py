# Segment Tree Implementation


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.segment_tree = [0] * 4 * len(self.arr)
        self.build_segment_tree(0, len(self.arr) - 1, 0)

    def build_segment_tree(self, start, end, i):
        if start == end:
            self.segment_tree[i] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.segment_tree[i] = (
                self.build_segment_tree(start, mid, 2 * i + 1) +
                self.build_segment_tree(mid + 1, end, 2 * i + 2)
            )

        return self.segment_tree[i]

    def get_range_sum(self, i, j):
        return self._range_sum(i, j, 0, len(self.arr) - 1, 0)

    def _range_sum(self, q_start, q_end, seg_start, seg_end, seg_i):
        if seg_end < q_start or seg_start > q_end:
            return 0
        elif seg_start >= q_start and seg_end <= q_end:
            return self.segment_tree[seg_i]
        else:
            mid = (seg_start + seg_end) // 2
            return (
                self._range_sum(q_start, q_end, seg_start, mid, 2 * seg_i + 1) +
                self._range_sum(q_start, q_end, mid + 1, seg_end, 2 * seg_i + 2)
            )

    def update(self, i, val):
        diff = val - self.arr[i]
        self.arr[i] = val
        self.perform_update(0, len(self.arr) - 1, diff, i, 0)

    def perform_update(self, seg_start, seg_end, diff, i, seg_i):
        if i < seg_start or i > seg_end:
            return
        self.segment_tree[seg_i] += diff
        if seg_start < seg_end:
            mid = (seg_start + seg_end) // 2
            self.perform_update(seg_start, mid, diff, i, 2 * seg_i + 1)
            self.perform_update(mid + 1, seg_end, diff, i, 2 * seg_i + 2)


if __name__ == '__main__':

    actions = [
        "NumArray", "sumRange", "sumRange", "sumRange", "update", "update",
        "update", "sumRange", "update", "sumRange", "update"
    ]
    items = [
        [[0, 9, 5, 7, 3]], [4, 4], [2, 4], [3, 3], [4, 5], [1, 7],
        [0, 8], [1, 2], [1, 9], [4, 4], [3, 4]
    ]

    ans = []
    for i, action in enumerate(actions):
        if action == 'NumArray':
            st = SegmentTree(items[i][0])
        elif action == 'sumRange':
            ans.append(st.get_range_sum(items[i][0], items[i][1]))
        else:
            ans.append(st.update(items[i][0], items[i][1]))

    print(ans)
