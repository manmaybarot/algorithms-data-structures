# Construction of a binary tree using
# 1.) Inorder and Preorder
# 2.) Inorder and Postorder

from .travalsal import TreeNode

def build_bt_from_inorder_preorder(inorder, preorder):
    mapping = {}
    preindex = 0
    for i,j in enumerate(inorder):
        mapping[j] = i

    def build(start, end):
        nonlocal preindex
        if start>end: return

        root = TreeNode(preorder[preindex])
        preindex += 1

        if not root: return

        if start == end:
            return root

        index = mapping[root.val]

        root.left = build(start, index - 1)
        root.right = build(index + 1, end)

        return root

    return build(0, len(preorder)-1)


def build_bt_from_inorder_postorder(inorder, postorder):
    index_of = {}
    postindex = len(postorder) - 1
    for i, j in enumerate(inorder):
        index_of[j] = i

    def build(start, end):
        nonlocal postindex
        if start > end: return

        root = TreeNode(postorder[postindex])

        postindex -= 1

        if not root: return

        if start == end: return root

        index = index_of[root.val]

        root.right = build(index+1, end)
        root.left = build(start, index-1)

        return root

    return build(0, len(postorder)-1)
