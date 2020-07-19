# Find connected components in an undirected graph

import collections


def get_connected_components(pairs):
    graph = collections.defaultdict(list)
    for s, d in pairs:
        graph[s].append(d)
        graph[d].append(s)

    visited = set()
    parent = {}
    ans = False
    connected = []
    ans = []

    def dfs(vertex):
        nonlocal ans, visited, graph, parent, connected
        connected.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                dfs(neighbour)

    for vertex in graph.keys():
        if vertex not in visited:
            visited.add(vertex)
            dfs(vertex)
            ans.append(connected)
            connected = []

    return ans


if __name__ == '__main__':
    pairs = [('A', 'B'), ('B', 'C'), ('D', 'F'), ('D', 'E'), ('E', 'Z')]
    print(get_connected_components(pairs))
