# Binary Search Tree Implementation

from tree.traversal import Morristraversal


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if not node:
            return Node(val)
        elif val <= node.val:
            node.left = self._insert(val, node.left)
        else:
            node.right = self._insert(val, node.right)
        return node

    def sorted_print(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        print(node.val)  # visiting node
        self._inorder(node.right)


if __name__ == '__main__':
    bst = BST()

    values = [3, 8, 5, 3, 7, 7, 8, 1, 5]
    for val in values:
        bst.insert(val)

    print(Morristraversal().inorder(bst.root))
