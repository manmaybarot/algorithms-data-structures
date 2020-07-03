
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


class WithoutRecursion:
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
