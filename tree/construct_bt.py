# Construction of a binary tree using
# 1.) Inorder and Preorder
# 2.) Inorder and Postorder

from traversal import TreeNode


def build_bt_from_inorder_preorder(inorder, preorder):
    pre_idx = 0
    mapping = {}
    for idx, value in enumerate(inorder):
        mapping[value] = idx

    def build(left, right):
        nonlocal pre_idx
        if left > right:
            return None

        root = TreeNode(preorder[pre_idx])
        pre_idx += 1

        if left == right:
            return root

        in_idx = mapping[root.val]

        root.left = build(left, in_idx - 1)
        root.right = build(in_idx + 1, right)

        return root

    return build(0, len(inorder) - 1)


def build_bt_from_inorder_postorder(inorder, postorder):
    index_of = {}
    postindex = len(postorder) - 1
    for i, j in enumerate(inorder):
        index_of[j] = i

    def build(start, end):
        nonlocal postindex
        if start > end:
            return

        root = TreeNode(postorder[postindex])
        postindex -= 1

        if start == end:
            return root

        post_idx = index_of[root.val]

        root.right = build(post_idx + 1, end)
        root.left = build(start, post_idx - 1)

        return root

    return build(0, len(postorder) - 1)


def build_bt_from_pre_post(pre, post):
    if not pre:
        return
    seen = {pre[0]}

    post_index_of, pre_index_of = {}, {}
    for i in range(len(post)):
        post_index_of[post[i]] = i
        pre_index_of[pre[i]] = i

    def build(root):
        root_value = root.val
        print(root_value)
        possible_left = pre_index_of[root_value] + 1
        if possible_left < len(pre):
            if pre[possible_left] not in seen:
                seen.add(pre[possible_left])
                root.left = TreeNode(pre[possible_left])

        possible_right = post_index_of[root_value] - 1
        if possible_right >= 0:
            if post[possible_right] not in seen:
                seen.add(post[possible_right])
                root.right = TreeNode(post[possible_right])

        if root.left:
            build(root.left)
        if root.right:
            build(root.right)

        return root

    return build(TreeNode(pre[0]))
