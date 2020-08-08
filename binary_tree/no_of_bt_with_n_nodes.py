# Get numebr of binary trees can be formed
# using n nodes

# Recurrence Relation:
# T(n) = T(0)T(n-1) + T(1)T(n-2) + T(2)T(n-3)+ ... + T(n)T(0)

def get_number_of_bt(n):
    t = {}
    t[0] = 1
    t[1] = 1

    for i in range(2, n+1):
        for j in range(0, i):
            t[i] = t.get(i, 0) + t[j] * t[i-j-1]
            # T(2) = T(0)T(1) + T(1)T(0)
    return t[n]

if __name__ == '__main__':
    print(get_number_of_bt(4))
    print(get_number_of_bt(5))
