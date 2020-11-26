# Prim's Minimum Spanning Tree

class Heap():
    def __init__(self):
        self.heap_map = {}

    def heap_push(self, A, x):
        A.append(x)
        self.heap_map[x] = len(A) - 1
        parent_pos = (self.heap_map[x] - 1) // 2
        while len(A) > parent_pos >= 0:
            if A[parent_pos] > x:
                self.swap(A, x, A[parent_pos])
                parent_pos = (self.heap_map[x] - 1) // 2
            else:
                break

    def swap(self, A, x, y):
        self.heap_map[y], self.heap_map[x] = self.heap_map[x], self.heap_map[y]
        A[self.heap_map[x]], A[
            self.heap_map[y]
        ] = A[self.heap_map[y]], A[self.heap_map[x]]

    def heapify(self, A, i):
        left = (2 * i) + 1
        right = left + 1

        if left >= len(A):
            return
        elif right > len(A):
            if A[left] < A[i]:
                self.swap(A, A[left], A[i])
                self.heapify(A, left)
        else:
            if A[i] > A[left] >= A[right]:
                self.swap(A, A[right], A[i])
                self.heapify(A, right)
            elif A[i] > A[right] >= A[left]:
                self.swap(A, A[left], A[i])
                self.heapify(A, left)

    def heap_pop(self, A, x=None):
        if not x:
            i = 0
        else:
            i = self.heap_map[x]
        if len(A) == 1:
            return A.pop()
        else:
            min_element = A[i]
            A[i] = A.pop()
            self.heap_map[A[i]] = i
            self.heap_map.pop(min_element)
            self.heapify(A, i)
            return min_element


def get_mst(G, E):
    heap = Heap()
    A = []
    edge_to_weight = {}
    for g, e in zip(G, E):
        edge_to_weight[g] = e

    neighbours = {}
    for u, v in G:
        if u not in neighbours:
            neighbours[u] = [v]
        else:
            neighbours[u].append(v)
        if v not in neighbours:
            neighbours[v] = [u]
        else:
            neighbours[v].append(u)

    active = set()
    root = g[0]
    active.add(root)
    for nei in neighbours[root]:
        edge = (root, nei) if (root, nei) in edge_to_weight else (nei, root)
        heap.heap_push(A, (edge_to_weight[edge], edge))

    ans = []
    while A:
        w, edge = heap.heap_pop(A)
        node = edge[0] if edge[0] not in active else edge[1]
        active.add(node)
        for nei in neighbours[node]:
            e = (node, nei) if (node, nei) in edge_to_weight else (nei, node)
            if nei not in active:
                heap.heap_push(A, (edge_to_weight[e], e))
            else:
                if (edge_to_weight[e], e) in heap.heap_map:
                    heap.heap_pop(A, (edge_to_weight[e], e))
        ans.append(edge)

    return ans


if __name__ == '__main__':
    G = [
        (1, 3), (1, 2), (2, 4), (7, 8), (3, 4), (2, 5), (5, 7), (5, 6), (6, 8)
    ]
    E = [7, 1, 5, 4, 2, 6, 9, 3, 8]

    print(get_mst(G, E))

# O((V+E)log V)
