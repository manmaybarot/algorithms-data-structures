# Heap implementation with access to an index of element
# in O(1) time

import collections


class Node:
    def __init__(self, val):
        self.val = val


class NodeHeapMap:
    def __init__(self):
        self.nodeheap_map = collections.defaultdict()

    def heapify(self, A):
        """Heapify operation (Nlog(N))."""
        for i in range(len(A) // 2, -1, -1):  # due to nature of child indeces
            self._bubble_down(A, i)

    def heap_push(self, A, node):
        """heapmap bubble up operatuon."""
        A.append(node)
        i = len(A) - 1
        self.nodeheap_map[node] = i

        parent_of_i = (i - 1) // 2
        while parent_of_i >= 0:
            if A[parent_of_i].val > A[i].val:
                self._swap(A, parent_of_i, i)
                i = parent_of_i
                parent_of_i = (i - 1) // 2
            else:
                break

    def peek(self, A):
        """Get top element."""
        if len(A) > 0:
            return A[0]
        else:
            raise IndexError('heapmap is empty!')

    def heap_pop(self, A, node=None):
        """Remove and get top element."""
        if len(A) == 0:
            raise IndexError('heapmap is empty!')

        i = 0 if not node else self.nodeheap_map[node]
        removed = A[i]

        self._swap(A, i, len(A) - 1)

        A.pop()
        self.nodeheap_map.pop(removed)

        if len(A) > 1:
            self._bubble_down(A, i)

        return removed

    def _swap(self, A, i, j):
        """heapmap swap of elements and indeces."""

        (
            self.nodeheap_map[A[i]],
            self.nodeheap_map[A[j]]
        ) = self.nodeheap_map[A[j]], self.nodeheap_map[A[i]]

        A[i], A[j] = A[j], A[i]

    def _bubble_down(self, A, i):
        """heapmap bubble down operatuon."""
        left = (2 * i) + 1
        right = (2 * i) + 2

        if left < len(A):
            if right >= len(A):
                if A[i].val > A[left].val:
                    self._swap(A, i, left)
                    self._bubble_down(A, left)
            else:
                if A[left].val <= A[right].val and A[left].val < A[i].val:
                    self._swap(A, i, left)
                    self._bubble_down(A, left)
                elif A[right].val <= A[left].val and A[right].val < A[i].val:
                    self._swap(A, i, right)
                    self._bubble_down(A, right)
