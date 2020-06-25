# Infix to prefix

def convert_infix_to_prefix(infix):
    def is_right_parenthesis(t):
        return t == ')'

    def is_left_parenthesis(t):
        return t == '('

    def is_operand(t):
        return t not in {'+', '-', '*', '/', '(', ')', '^'}

    def current_lte_top(curr, top):
        return top in precedence and precedence[curr] <= precedence[top]

    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
    prefix = ''
    stack = []
    for i in infix[::-1].replace(' ', ''):
        if is_operand(i):
            prefix += i
        elif is_right_parenthesis(i):
            stack.append(i)
        elif is_left_parenthesis(i):
            top = stack.pop()
            while not is_right_parenthesis(top):
                prefix += top
                top = stack.pop()
        else:
            while stack and current_lte_top(i, stack[-1]):
                prefix += stack.pop()
            stack.append(i)
    if stack:
        prefix += ''.join(stack[::-1])
    return prefix[::-1]


if __name__ == '__main__':
    infix = 'K+L-M*N+(O^P)*W/U/V*T+Q'
    # infix = '(A + B) * (C + D)'
    print(convert_infix_to_prefix(infix))
