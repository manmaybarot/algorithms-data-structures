# verify if preorder for vinary search tree is valid:

from typing import List


def verifyPreorder(self, preorder: List[int]) -> bool:
    if not preorder:
        return True
    current = 0

    def verify(minimum, maximum):
        nonlocal current
        if current == len(preorder):
            return True

        root_val = preorder[current]

        if root_val < minimum or root_val > maximum:
            return False
        current += 1
        return verify(minimum, root_val - 1) or verify(root_val + 1, maximum)

    return verify(float('-inf'), float('inf'))
