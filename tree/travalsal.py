
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
