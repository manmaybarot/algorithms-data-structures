# Prefix to infix

def convert_prefix_to_infix(prefix):
    operand_stack = []
    prefix = prefix[::-1]
    for i in prefix:
        if i in {'+', '-', '*', '^', '/'}:
            first = operand_stack.pop()
            second = operand_stack.pop()
            operand_stack.append(first + i + second)
        else:
            operand_stack.append(i)

    return operand_stack[0]


if __name__ == '__main__':
    prefix = '+K-L+*MN+*^OP/W/U*VTQ'
    print(convert_prefix_to_infix(prefix))
