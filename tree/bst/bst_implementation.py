# Binary Search Tree Implementation

from tree.traversal import Morristraversal


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.p = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node, p=None):
        if not node:
            node = Node(val)
            node.p = p
            return node
        elif val < node.val:
            node.left = self._insert(val, node.left, node)
        else:
            node.right = self._insert(val, node.right, node)
        return node

    def delete(self, key, root):
        if root is None:
            return
        elif key < root.val:
            root.left = self.delete(key, root.left)
        elif key > root.val:
            root.right = self.delete(key, root.right)
        else:
            if root.left is None:
                if root.right:
                    root.right.p = root.p
                return root.right
            elif root.right is None:
                if root.left:
                    root.left.p = root.p
                return root.left
            else:
                inorder_successor = root.right
                while inorder_successor.left:
                    inorder_successor = inorder_successor.left

                root.val = inorder_successor.val
                root.right = self.delete(inorder_successor.val, root.right)

        return root


if __name__ == '__main__':
    bst = BST()

    values = [3, 8, 5, 3, 7, 7, 8, 1, 5]
    for val in values:
        bst.insert(val)

    print(Morristraversal().inorder(bst.root))

    bst.delete(7, bst.root)

    print(Morristraversal().inorder(bst.root))
