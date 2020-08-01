import collections


def detect_cycle(pairs):
    graph = collections.defaultdict(list)
    for s, d in pairs:
        graph[s].append(d)
        graph[d].append(s)

    visited = set()
    parent = {}
    is_cycle = False
    cycle = []

    def dfs(vertex):
        nonlocal is_cycle, visited, graph, parent, cycle
        if is_cycle:
            return
        for neighbour in graph[vertex]:
            if is_cycle:
                return
            if neighbour in visited and parent[vertex] != neighbour:
                is_cycle = True
                while vertex != neighbour:
                    cycle.append(vertex)
                    vertex = parent[vertex]
                cycle.append(neighbour)
                return
            elif neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = vertex
                dfs(neighbour)

    for vertex in graph.keys():
        if is_cycle:
            return is_cycle, cycle
        elif vertex not in visited:
            if vertex not in parent:
                parent[vertex] = None
            visited.add(vertex)
            dfs(vertex)

    return is_cycle, cycle


if __name__ == '__main__':
    pairs = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'B')]
    print(detect_cycle(pairs))
