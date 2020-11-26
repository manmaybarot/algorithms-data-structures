# Shortest Path Algorithm: Dijkstra

import collections
import heapq


def get_sssp(G, E, source):
    d = {}
    weight = {}
    for u, v in G:
        weight[(u, v)] = E.pop(0)
        if u not in d:
            d[u] = float('inf')
        if v not in d:
            d[v] = float('inf')

    d[source] = 0
    parent = {}
    relaxed_vertices = set(source)

    neighbours = collections.defaultdict(list)
    for u, v in G:
        neighbours[u].append(v)

    def relaxation(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    q = [(0, source)]
    heapq.heapify(q)

    while q:
        w, v = heapq.heappop(q)

        for nei in neighbours[v]:
            if nei not in relaxed_vertices:
                relaxation(v, nei, weight[(v, nei)])
                heapq.heappush(q, (weight[(v, nei)], nei))

        relaxed_vertices.add(v)

    return parent


if __name__ == '__main__':
    G = [
        ('A', 'D'), ('A', 'C'), ('D', 'C'), ('C', 'B'), ('B', 'A')
    ]
    E = [1, 2, 1, 2, 3]

    print(get_sssp(G, E, source='A'))
