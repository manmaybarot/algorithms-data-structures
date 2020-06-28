from travalsal import TreeNode, postorder

def construct_expression_tree(postfix):
    stack = []
    for i in postfix:
        if i in {'+','*','-','/','^'}:
            right = stack.pop()
            left = stack.pop()
            new_node = TreeNode(i)
            new_node.left = left
            new_node.right = right
            stack.append(new_node)
        else:
            stack.append(TreeNode(i))

    return stack[0]


if __name__ == '__main__':
    postfix = 'KL+MN*-OP^W*U/V/T*+Q+'
    root = construct_expression_tree(postfix)
    print(postorder(root))
