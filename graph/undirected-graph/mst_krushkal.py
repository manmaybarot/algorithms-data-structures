# Union-find and Union-find


class Node():
    def __init__(self):
        self.root = self
        self.rank = 0


def union(x, y):
    if x.rank == y.rank:
        x.rank += 1
        y.root = x
    elif x.rank < y.rank:
        x.root = y
    else:
        y.root = x


def find(x):
    if x != x.root:
        x.root = find(x.root)
    return x.root


def krushkal_mst(G, W, r):
    mapping = {}

    def make_set(x):
        if x not in mapping:
            mapping[x] = Node()

    for u, v in G:
        make_set(u)
        make_set(v)

    weight_dict = {}
    for w, g in zip(W, G):
        if w in weight_dict:
            weight_dict[w].append(g)
        else:
            weight_dict[w] = [g]

    G_prime = []
    for e in sorted(weight_dict.keys()):
        for item in weight_dict[e]:
            G_prime.append(item)

    mst = []
    for u, v in G_prime:
        u_parent = find(mapping[u])
        v_parent = find(mapping[v])
        if u_parent != v_parent:
            union(u_parent, v_parent)
            mst.append((v, u))

    # w = {}
    # for g, e in zip(G, W):
    #     w[g] = e
    #     w[g[::-1]] = e
    # total_weight = 0
    # for j in mst:
    #     total_weight += w[j]
    # print(total_weight)

    return mst


if __name__ == '__main__':
    G = [
        (1, 3), (1, 2), (2, 4), (7, 8), (3, 4), (2, 5), (5, 7), (5, 6), (6, 8)
    ]
    W = [7, 1, 5, 4, 2, 6, 9, 3, 8]
    r = 1

    # G = [
    #     (1, 3), (1, 2), (2, 4), (7, 8), (3, 4)
    # ]
    # W = [7, 1, 5, 4, 2]
    # r = 4

    # G = [
    #     (1, 3), (1, 2), (2, 3)
    # ]
    # W = [7, 1, 5]
    # r = 3

    print(krushkal_mst(G, W, r))

# Time Complexity: O([E log* V] + [E log E])
# (** where usually value of log* V does not exceed
# more then 5 (4 in case of α(n))

# Hence, Time: O(E log E)

# Space: O(|E| + |V|)
# (E for sorting edges, V for maintaining roots in Union-Find)
# (E >= V - 1) ==> Space: O(|E|)
