# Postfix to infix

def convert_postfix_to_infix(postfix):
    operand_stack = []
    for i in postfix:
        if i in {'+', '-', '*', '^', '/'}:
            second = operand_stack.pop()
            first = operand_stack.pop()
            operand_stack.append(first + i + second)
        else:
            operand_stack.append(i)

    return operand_stack[0]


if __name__ == '__main__':
    postfix = 'KL+MN*-OP^W*U/V/T*+Q+'
    print(convert_postfix_to_infix(postfix))
