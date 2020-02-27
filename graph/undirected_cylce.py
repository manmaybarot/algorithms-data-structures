import collections

def is_cycle(pairs):
    graph = collections.defaultdict(list)
    for s, d in pairs:
        graph[s].append(d)
        graph[d].append(s)

    visited = set()
    parent = {}
    ans = False

    def dfs(vertex):
        nonlocal ans, visited, graph, parent
        if ans:
            return
        for neighbour in graph[vertex]:
            # if we see parent of vertex,
            # we should'nt go that way
            if neighbour == parent[vertex]:
                continue
            if neighbour in visited and parent[neighbour] != vertex:    
                ans = True
                break
            elif neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = vertex
                dfs(neighbour)

    for vertex in graph.keys():
        if ans:
            return ans
        if vertex not in visited:
            if not parent:
                parent[vertex] = 'start_'
            visited.add(vertex)
            dfs(vertex)

    return ans

if __name__=='__main__':
    pairs = [('A', 'B'), ('B', 'C'), ('C', 'A'),('D', 'E')]
    print(is_cycle(pairs))
