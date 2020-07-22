# Your class will have one method, book(int start, int end).
# Formally, this represents a booking on the half
# open interval [start, end), the range of real
# numbers x such that start <= x < end.

# A K-booking happens when K events have some non-empty
# intersection (ie., there is some time that is common
# to all K events.)

# For each call to the method MyCalendar.book, return
# an integer K representing the largest integer such
# that there exists a K-booking in the calendar.

# Using Lazy Update

class MyCalendarThree:

    def __init__(self):
        self.tree = collections.defaultdict()
        self.lazy_tree = collections.defaultdict()

    def book(self, start: int, end: int) -> int:
        self.update(
            range_start=start,
            range_end=end - 1,
            i=0,
            tree_start=0,
            tree_end=1000000000)
        return self.tree.get(0, 0) + self.lazy_tree.get(0, 0)

    def update(self, range_start, range_end, i, tree_start, tree_end):

        if tree_start > tree_end:
            return

        # lazy_update
        if self.lazy_tree.get(i, 0) != 0:
            self.tree[i] = self.tree.get(i, 0) + self.lazy_tree[i]
            if tree_start != tree_end:  # not a leaf node
                self.lazy_tree[2 * i + \
                    1] = self.lazy_tree.get(2 * i + 1, 0) + self.lazy_tree[i]
                self.lazy_tree[2 * i + \
                    2] = self.lazy_tree.get(2 * i + 2, 0) + self.lazy_tree[i]
            self.lazy_tree.pop(i)

        # no overlap
        if range_start > tree_end or range_end < tree_start:
            return

        # full overlap
        if range_start <= tree_start and tree_end <= range_end:
            self.tree[i] = self.tree.get(i, 0) + 1
            if tree_start != tree_end:
                self.lazy_tree[2 * i +
                               1] = self.lazy_tree.get(2 * i + 1, 0) + 1
                self.lazy_tree[2 * i +
                               2] = self.lazy_tree.get(2 * i + 2, 0) + 1
            return

        # partial overlap
        mid = (tree_start + tree_end) // 2
        self.update(range_start, range_end, 2 * i + 1, tree_start, mid)
        self.update(range_start, range_end, 2 * i + 2, mid + 1, tree_end)

        self.tree[i] = max(
            self.tree.get(
                2 * i + 1,
                0),
            self.tree.get(
                2 * i + 2,
                0))


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
