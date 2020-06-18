
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(node):
    if not node: return

    inorder(node.left)
    print(node.val) # visiting node
    inorder(node.right)


