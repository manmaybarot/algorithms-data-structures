# Prim's Minimum Spanning Tree

from collections import defaultdict


class MinHeap:
    def __init__(self):
        self.edge_map = {}

    def heapify(self, Q):
        mid = len(Q) //2
        for i in reversed(range(mid)):
            self._shift_down(i, Q)

    def heap_push(self, Q, node):
        Q.append(node)
        edge = node[1]
        self.edge_map[edge] = len(Q) - 1
        self._shift_up(self.edge_map[edge], Q)

    def heap_pop(self, Q, edge):
        if edge in self.edge_map:
            i = self.edge_map[edge]
            self._swap(i, len(Q) - 1, Q)
            Q.pop()
            self._shift_down(i, Q)
            self.edge_map.pop(edge)

    def pop_min(self, Q):
        top = Q[0]
        self._swap(0, len(Q) - 1, Q)
        Q.pop()
        self._shift_down(0, Q)
        self.edge_map.pop(top[1])
        return top[1]

    def _shift_down(self, i, Q):
        left_child = (i + 1) // 2
        right_child = left_child + 1

        while i < len(Q):
            current = Q[i]
            if right_child < len(Q):
                left = Q[left_child]
                right = Q[right_child]

                if left < current and left <= right:
                    self._swap(i, left_child, Q)
                    i = left_child
                elif right < current and right <= left:
                    self._swap(i, right_child, Q)
                    i = right_child
                else:
                    break
            elif left_child < len(Q):

                left = Q[left_child]
                if left < current:
                    self._swap(i, left_child, Q)
                    i = left_child
                else:
                    break
            else:
                break
            left_child = (i + 1) // 2
            right_child = left_child + 1

    def _shift_up(self, i, Q):
        parent = (i - 1) // 2

        while parent >= 0:
            p_node = Q[parent]
            child_node = Q[i]
            if p_node[0] > child_node[0]:
                self._swap(parent, i, Q)
                i = parent
                parent = (i - 1) // 2
            else:
                break

    def _swap(self, i, j, Q):
        Q[i], Q[j] = Q[j], Q[i]
        self.edge_map[Q[i][1]], \
        self.edge_map[Q[j][1]] = self.edge_map[Q[j][1]], self.edge_map[Q[i][1]]


def get_mst(G, W, r):
    processed = set()
    processed.add(r)

    neighbours = defaultdict(list)
    for u, v in G:
        neighbours[u].append(v)
        neighbours[v].append(u)

    min_heap = MinHeap()
    q = []

    w = {}
    for g, e in zip(G, W):
        w[g] = e
        w[g[::-1]] = e

    for u in neighbours[r]:
        min_heap.heap_push(q, (w[(r, u)], (r, u)))

    min_heap.heapify(q)
    mst = []
    while q:
        edge = min_heap.pop_min(q)
        v = edge[0] if edge[0] not in processed else edge[1]

        for u in neighbours[v]:
            e = (u, v)

            if u not in processed:
                min_heap.heap_push(q, (w[e], e))
            else:
                if e not in min_heap.edge_map:
                    e = e[::-1]
                min_heap.heap_pop(q, e)

        processed.add(v)
        mst.append(edge)

    # total_weight = 0
    # for j in mst:
    #     total_weight += w[j]
    # print(total_weight)

    return mst


if __name__ == '__main__':
    G = [
        (1, 3), (1, 2), (2, 4), (7, 8), (3, 4), (2, 5), (5, 7), (5, 6), (6, 8)
    ]
    W = [7, 1, 5, 4, 2, 6, 9, 3, 8]
    r = 1

    # G = [
    #     (1, 3), (1, 2), (2, 4), (7, 8), (3, 4)
    # ]
    # W = [7, 1, 5, 4, 2]
    # r = 4

    # G = [
    #     (1, 3), (1, 2), (2, 3)
    # ]
    # W = [7, 1, 5]
    # r = 3

    print(get_mst(G, W, r))


# pop_min operation takes log V which runs for V nodes
# inner for loop runs 2 * E time and each push/pop operation takes log V
# O((|V| + |E|)log V)

# Space: O(|V| + |E|)
