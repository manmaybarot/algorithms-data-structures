from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# a + b
def inorder(node):
    if not node: return

    inorder(node.left)
    print(node.val) # visiting node
    inorder(node.right)

# + a b
def preorder(node):
    if not node: return

    print(node.val) # visiting node
    preorder(node.left)
    preorder(node.right)


# a b +
def postorder(node):
    if not node: return

    postorder(node.left)
    postorder(node.right)
    print(node.val)


class IterativeTravalsalWithStack:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
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

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = []
        while stack:
            curr = stack.pop()
            if curr:
                ans.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)

        return ans

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = []
        while stack:
            root = stack.pop()
            if root:
                stack.append(root.left)
                stack.append(root.right)
                ans.append(root.val)
        return ans[::-1]


class MorrisTravalsal:
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
                while predecesor.right:
                    predecesor = predecesor.right
                predecesor.right = current
                current.left = None
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
