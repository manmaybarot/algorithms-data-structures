# Union-find and Union-find


class Node():
    def __init__(self):
        self.root = self
        self.rank = 0

def union(x, y):
    if x.rank == y.rank:
        x.rank+=1
        y.root = x
    elif x.rank < y.rank:
        x.root= y
    else:
        y.root= x

def find(x):
    if x != x.root:
        x.root = find(x.root)
    return x.root

def krushkal_mst(G,E):
    mapping = {}

    def make_set(x):
        if x not in mapping:
            mapping[x] = Node()

    for u, v in G:
        make_set(u)
        make_set(v)

    weight_dict = {}
    for e, g in zip(E, G):
        if e in weight_dict:
            weight_dict[e].append(g)
        else:
            weight_dict[e] = [g]

    G_prime = []
    for e in sorted(weight_dict.keys()):
        for item in weight_dict[e]:
            G_prime.append(item)

    mst = []
    for u,v in G_prime:
        u_parent = find(mapping[u])
        v_parent = find(mapping[v])
        if  u_parent != v_parent:
            union(u_parent, v_parent)
            mst.append((u,v))

    return mst

if __name__=='__main__':
    G = [
        (1, 3), (1, 2), (2, 4), (7, 8), (3, 4), (2, 5), (5, 7), (5, 6), (6, 8)
    ] 
    E = [7, 1, 5, 4, 2, 6, 9, 3, 8]

    # G = [
    #     (1, 3), (1, 2), (2, 4), (7, 8), (3, 4)
    # ] 
    # E = [7, 1, 5, 4, 2]
    # G = [
    #     (1, 3), (1, 2), (2, 3)
    # ] 
    # E = [7, 1, 5]

    print(krushkal_mst(G, E))
