# Segment Tree Implementation


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.segment_tree = [0] * 4*len(self.arr)
        self.build_segment_tree(0, len(self.arr)-1, 0)

    def build_segment_tree(self, start, end, i):
        if start == end:
            self.segment_tree[i] = self.arr[start]
        else:
            mid = (start + end)//2
            self.segment_tree[i] = (
                self.build_segment_tree(start, mid, 2*i+1) +
                self.build_segment_tree(mid+1, end, 2*i+2)
            )

        return self.segment_tree[i]

    def get_range_sum(self, i, j):
        return self.range_sum(i, j, 0, len(self.arr)-1, 0)

    def range_sum(self, q_start, q_end, seg_start, seg_end, seg_i):
        if seg_end < q_start or seg_start > q_end:
            return 0
        elif seg_start >= q_start and seg_end <= q_end:
            return self.segment_tree[seg_i]
        else:
            mid = (seg_start + seg_end)//2
            return (
                self.range_sum(q_start, q_end, seg_start, mid, 2*seg_i+1) +
                self.range_sum(q_start, q_end, mid+1, seg_end, 2*seg_i+2)
            )

    def update(self, i, val):
        self.update_segment_tree(0, len(self.segment_tree)-1, i, val-self.arr[i])

    def update_segment_tree(self, seg_start, seg_end, i, diff):
        if seg_start <= i <= seg_end:
            self.segment_tree[i] += diff
            mid = (seg_start + seg_end)//2
            self.update_segment_tree(seg_start, mid, 2*i+1, diff)
            self.update_segment_tree(mid+1, seg_end, 2*i+2, diff)


if __name__=='__main__':
    st = SegmentTree([10, 20, 30, 40])

    print(st.get_range_sum(0, 2))
    st.update(1,500)
    print(st.get_range_sum(0, 2))
