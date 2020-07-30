# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        x = y = pred = current_pred = None

        while root:
            if root.left:
                current_pred = root.left
                while current_pred.right and current_pred.right != root:
                    current_pred = current_pred.right

                if current_pred.right is None:
                    current_pred.right = root
                    root = root.left
                else:
                    if pred and pred.val > root.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root
                    current_pred.right = None
                    root = root.right
            else:
                if pred and pred.val > root.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root
                root = root.right

        x.val, y.val = y.val, x.val
