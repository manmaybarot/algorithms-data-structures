# Topological Sort
from collections import deque


def topological_sort(prerequisites):
    graph = {}
    for course, pre in prerequisites:
        if course in graph:
            graph[course].append(pre)
        else:
            graph[course] = [pre]
        if pre not in graph:
            graph[pre] = []

    topology = deque([])
    visited = set()

    def dfs(vertex):
        for nei in graph[vertex]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)
        topology.appendleft(vertex)

    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(vertex)

    return topology


if __name__ == '__main__':
    prerequisites = [(1, 2), (1, 3), (2, 3), (2, 4), (4, 3), (4, 5), (3, 5)]
    print(topological_sort(prerequisites))

# O(V+E)
