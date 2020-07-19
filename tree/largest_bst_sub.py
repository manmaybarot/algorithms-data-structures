# Sum of the nodes of a largest BST
# All of children including parent shoud be BST

from travalsal import TreeNode


def largestBSTSubtree(self, root: TreeNode) -> int:
    if not root:
        return 0

    def postorder(node):
        if not node.left and not node.right:
            return True, 1, node.val, node.val
        else:
            if node.left:
                left_bst, left_count, left_min, left_max = postorder(
                    node.left
                )
            if node.right:
                right_bst, right_count, right_min, right_max = postorder(
                    node.right
                )

            if node.left and node.right:
                if left_bst and right_bst:
                    if left_max < node.val < right_min:
                        return (
                            True,
                            left_count + right_count + 1,
                            left_min,
                            right_max
                        )
                return False, max(left_count, right_count), 0, 0
            elif node.right:
                if right_bst:
                    if node.val < right_min:
                        return True, right_count + 1, node.val, right_max
                return False, right_count, 0, 0
            else:
                if left_bst:
                    if node.val > left_max:
                        return True, left_count + 1, left_min, node.val
                return False, left_count, 0, 0


# is_bst, ans, _, __ = postorder(root)
# return ans
