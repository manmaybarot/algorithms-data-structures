# KosaRaju's Algorithm

def get_connected_components(pairs):
    graph = {}
    for s, d in pairs:
        if s in graph:
            graph[s].append(d)
        else:
            graph[s] = [d]
        if d not in graph:
            graph[d] = []

    descreasing_ft = []
    visited = set()

    def dfs(vertex, g):
        nonlocal visited, descreasing_ft
        for nei in g[vertex]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei, g)
        descreasing_ft.insert(0, vertex)

    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(vertex, graph)

    graph_t = {}
    for s, d in graph.items():
        for nei in d:
            if nei not in graph_t:
                graph_t[nei] = [s]
            else:
                graph_t[nei].append(s)
        if s not in graph_t:
            graph_t[s] = []

    visited = set()
    ans = []

    decreasing_time = descreasing_ft[:]
    descreasing_ft = []
    for vertex in decreasing_time:
        if vertex not in visited:
            visited.add(vertex)
            dfs(vertex, graph_t)
            ans.append(descreasing_ft)
            descreasing_ft = []

    return ans

if __name__=='__main__':
    pairs = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (4, 6)]
    print(get_connected_components(pairs))
