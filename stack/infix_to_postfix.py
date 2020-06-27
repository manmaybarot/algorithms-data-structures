# Infix to postfix

def convert_infix_to_postfix(infix):
    def is_operand(t):
        return t not in {'+', '-', '*', '/', '(', ')', '^'}

    def is_left_parenthesis(t):
        return t == '('

    def is_right_parenthesis(t):
        return t == ')'

    def current_lte_top(curr, top):
        return top in precedence and precedence[curr] <= precedence[top]

    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    postfix = ''
    stack = []
    for i in infix.replace(' ', ''):
        if is_operand(i):
            postfix += i
        elif is_left_parenthesis(i):
            stack.append(i)
        elif is_right_parenthesis(i):
            top = stack.pop()
            while not is_left_parenthesis(top):
                postfix += top
                top = stack.pop()
        else:
            while stack and current_lte_top(i, stack[-1]):
                postfix += stack.pop()
            stack.append(i)
    if stack:
        postfix += ''.join(stack[::-1])

    return postfix


if __name__ == '__main__':
    infix = '5+23-5-(4-2)*(3^5(3+0))/12'
    # infix = '(A + B) * (C + D)'
    # infix = 'K+L-M*N+(O^P)*W/U/V*T+Q'
    print(convert_infix_to_postfix(infix))
