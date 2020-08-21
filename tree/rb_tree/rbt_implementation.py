# Red-Black Tree Implementation

from tree.traversal import Morristraversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.p = None
        self.color = None


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = 'black'
        self.root = self.nil

    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            x = x.left if z.val < x.val else x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = z.right = self.nil
        z.color = 'red'
        self._rb_insert_fixup(z)

    def _rb_insert_fixup(self, z):
        while z.p.color == 'red':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'red':
                    y.color = 'black'
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self._left_rotate(z)
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self._right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'red':
                    y.color = 'black'
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self._right_rotate(z)
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self._left_rotate(z.p.p)
        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y

    def rb_inorder(self, q):
        if q != self.nil:
            self.rb_inorder(q.left)
            print(q.val)
            self.rb_inorder(q.right)

    def _rb_transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

if __name__ == '__main__':
    rb_tree = RedBlackTree()

    values = [3, 8, 5, 3, 7, 7, 8, 1, 5]
    for val in values:
        rb_tree.rb_insert(Node(val))
    print(rb_tree.rb_inorder(rb_tree.root))
