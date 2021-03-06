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

    def tree_minimum(self, r):
        while r.left != self.nil:
            r = r.left
        return r

    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self._rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'black':
            self._rb_delete_fixup(x)

    def _rb_transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def _rb_delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.p.left:
                w = x.p.right
                if w.color == 'red':
                    w.color = 'black'
                    w.p.color = 'red'
                    self._left_rotate(w.p)
                    w = x.p.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.p
                else:
                    if  w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._right_rotate(w)
                        w = x.p.right
                    w.color = w.p.color
                    w.p.color = 'black'
                    w.right.color = 'black'
                    self._left_rotate(w.p)
            else:
                w = x.p.left
                if w.color == 'red':
                    w.color = 'black'
                    w.p.color = 'red'
                    self._right_rotate(w.p)
                    w = x.p.left
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.p
                else:
                    if  w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._left_rotate(w)
                        w = x.p.left
                    w.color = w.p.color
                    w.p.color = 'black'
                    w.left.color = 'black'
                    self._right_rotate(w.p)
        x.color = 'black'


if __name__ == '__main__':
    rb_tree = RedBlackTree()

    values = [3, 8, 5, 3, 7, 7, 8, 1, 5]
    for val in values:
        rb_tree.rb_insert(Node(val))
    rb_tree.rb_delete(rb_tree.root.right)
    print(rb_tree.rb_inorder(rb_tree.root))
