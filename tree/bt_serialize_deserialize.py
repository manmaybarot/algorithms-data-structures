from .traversal import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ';'

        return (
            f"{root.val},{self.serialize(root.left)},"
            f"{self.serialize(root.right)}"
        )

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        q = collections.deque(data.split(','))

        return self.helper(q)

    def helper(self, q):
        node_val = q.popleft()
        if node_val == ';':
            return None

        node = TreeNode(node_val)
        node.left = self.helper(q)
        node.right = self.helper(q)

        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
