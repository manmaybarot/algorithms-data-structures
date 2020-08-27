from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class RecursiveTraversal:
    # a + b
    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)
        print(node.val)  # visiting node
        self.inorder(node.right)

    # + a b
    def preorder(self, node):
        if not node:
            return

        print(node.val)  # visiting node
        self.preorder(node.left)
        self.preorder(node.right)

    # a b +
    def postorder(self, node):
        if not node:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)


class IterativeWithStack:
    def inorder(self, root: TreeNode) -> List[int]:
        stack = collections.deque([])
        ans = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            ans.append(current.val)
            current = current.right
        return ans

    def preorder(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = []
        while stack:
            curr = stack.pop()
            if curr:
                ans.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)

        return ans

    def postorder(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = []
        while stack:
            root = stack.pop()
            if root:
                stack.append(root.left)
                stack.append(root.right)
                ans.append(root.val)
        return ans[::-1]


class Morristraversal:
    def inorder(self, root: TreeNode) -> List[int]:
        current = root
        ans = []
        while current:
            if not current.left:
                ans.append(current.val)
                current = current.right
            else:
                predecesor = current.left
                next_current = current.left
                while predecesor.right and predecesor.right != current:
                    predecesor = predecesor.right
                if predecesor.right == current:
                    predecesor.right = None
                    ans.append(current.val)
                    current = current.right
                else:
                    predecesor.right = current
                    current = next_current
        return ans

    def preorder(self, root: TreeNode) -> List[int]:
        current = root
        ans = []
        while current:
            ans.append(current.val)
            if not current.left:
                current = current.right
            else:
                predecesor = current.left
                next_current = current.left
                while predecesor.right:
                    predecesor = predecesor.right
                predecesor.right = current.right
                current.left = None
                current = next_current
        return ans

    def postorder(self, root: TreeNode) -> List[int]:
        current = root
        ans = []
        while current:
            ans.append(current.val)
            if not current.right:
                current = current.left
            else:
                predecesor = current.right
                next_current = current.right
                while predecesor.left:
                    predecesor = predecesor.left
                predecesor.left = current.left
                current.right = None
                current = next_current
        return ans[::-1]
