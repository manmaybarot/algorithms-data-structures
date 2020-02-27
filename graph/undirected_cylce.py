import collections

def is_cycle(pairs):
    graph = collections.defaultdict(list)
    for s, d in pairs:
        graph[s].append(d)
        graph[d].append(s)

    visited = set()
    parent = {}
    ans = False
    cycle = []

    def dfs(vertex):
        nonlocal ans, visited, graph, parent, cycle
        if ans:
            return
        for neighbour in graph[vertex]:
            if ans:
                return
            if neighbour in visited and parent[vertex] != neighbour:    
                ans = True
                while vertex and vertex != neighbour:
                    cycle.append(vertex)
                    vertex = parent[vertex]
                cycle.append(neighbour)
                return
            elif neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = vertex
                dfs(neighbour)

    for vertex in graph.keys():
        if ans:
            return ans, cycle
        elif vertex not in visited:
            if vertex not in parent:
                parent[vertex] = None
            visited.add(vertex)
            dfs(vertex)

    return ans, cycle

if __name__=='__main__':
    pairs = [('A', 'B'), ('B', 'C'), ('C', 'A'),('D', 'E')]
    print(is_cycle(pairs))
