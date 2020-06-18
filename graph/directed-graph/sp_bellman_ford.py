# Shortest Path Algorithm: Bellman Ford


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

    def relaxation(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    for i in range(len(d)-2):
        for u, v in G:
            relaxation(u, v, weight[(u, v)])

    for u, v in G:
        if d[v] > d[u] + weight[(u, v)]:
            return False

    return parent

if __name__=='__main__':
    G = [
        ('A', 'D'), ('A', 'C'), ('D', 'C'), ('C', 'B'), ('B', 'A')
    ] 
    E = [1, 2, 1, 2, 3]

    print(get_sssp(G, E, source='A'))

# O(VE)
