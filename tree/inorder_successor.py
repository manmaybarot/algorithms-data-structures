# Inorder successor of a node



# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def inorderSuccessor(self, node: 'Node') -> 'Node':
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor
    else:
        p = node
        while p.parent:
            if p.parent.left == p:
                return p.parent
            p = p.parent
        else:
            return None
