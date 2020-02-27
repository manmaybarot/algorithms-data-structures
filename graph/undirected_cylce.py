import collections

def is_cycle(pairs):
    graph = collections.defaultdict(list)
    for s, d in pairs:
        graph[s].append(d)
        graph[d].append(s)

    visited = set()
    ans = False

    def dfs(vertex, parent):
        nonlocal ans, visited, graph
        if ans:
            return
        for neighbour in graph[vertex]:
            if neighbour in visited and parent != neighbour:    
                ans = True
                break
            elif neighbour not in visited:
                visited.add(neighbour)
                dfs(neighbour, vertex)

    for vertex in graph.keys():
        if ans:
            return ans
        if vertex not in visited:
            visited.add(vertex)
            dfs(vertex, 'None')

    return ans

if __name__=='__main__':
    pairs = [('A', 'B'), ('B', 'C'), ('C', 'A'),('D', 'E')]
    print(is_cycle(pairs))
