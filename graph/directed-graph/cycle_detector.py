# Detect cycle in directed graph


def detect_cycle(pairs):
    graph = {}
    alarm = {}
    visited = set()
    is_cycle = False
    cycle = []

    for s, d in pairs:
        if s not in graph:
            graph[s] = [d]
        else:
            graph[s].append(d)
        if d not in graph:
            graph[d] = []

    for s in graph.keys():
        alarm[s] = False

    def dfs(vertex):
        nonlocal is_cycle

        if is_cycle:
            return
        alarm[vertex] = True
        for nei in graph[vertex]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)
            elif nei in visited and alarm[nei]:
                is_cycle = True
                for active in alarm:
                    if alarm[active]:
                        cycle.append(active)
                cycle.append(nei)
                return
        alarm[vertex] = False

    for v in graph:
        if is_cycle:
            return is_cycle, cycle
        if v not in visited:
            visited.add(v)
            dfs(v)

    return is_cycle, cycle


if __name__ == '__main__':
    pairs = [('A', 'B'), ('C', 'B'), ('C', 'A'), ('D', 'B')]
    print(detect_cycle(pairs))
    pairs = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'B')]
    print(detect_cycle(pairs))
