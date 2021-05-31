# Print all possible permutation of a given string


def permutations(A):
    seen = set()
    perm_print_helper(A, seen, '')


def perm_print_helper(A, seen, s):
    if len(s) == len(A):
        print(s)
        return

    for j in range(len(A)):
        if j not in seen:
            seen.add(j)
            s_temp = s + A[j]
            perm_print_helper(A, seen, s_temp)
            seen.remove(j)


if __name__ == '__main__':
    A = list('manmay')
    permutations(A)
