#

from traversal import TreeNode, Node


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return
        bt_root = TreeNode(root.val)
        q = collections.deque([(root, bt_root)])

        while q:
            nary_node, bt_node = q.popleft()
            previous_child = None
            first_child = None
            for child in nary_node.children:
                new_node = TreeNode(child.val)
                if previous_child:
                    previous_child.right = new_node
                else:
                    first_child = new_node
                previous_child = new_node
                q.append((child, new_node))
            bt_node.left = first_child

        return bt_root

        # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return
        root = Node(data.val, [])
        q = collections.deque([(root, data)])

        while q:
            nary_root, bt_root = q.popleft()
            child = bt_root.left
            while child:
                new_nary_node = Node(child.val, [])
                nary_root.children.append(new_nary_node)
                q.append((new_nary_node, child))
                child = child.right

        return root
