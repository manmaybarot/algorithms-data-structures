# Infix to postfix
from collections import deque

def convert_infix_to_postfix(s):
    def is_operand(t):
        return t not in {'+', '-', '*', '/', '(', ')'}

    def is_left_parenthesis(t):
        return t == '('

    def is_right_parenthesis(t):
        return t == ')'

    def current_lte_top(curr, top):
        return curr <= top

    stack = []
    postfix = ''
    for i in s:
        if is_operand(i):
            postfix += i
        else:
            if is_left_parenthesis(i):
                stack.append(i)
            elif stack and is_right_parenthesis(i):
                top = stack.pop()
                while stack and not is_left_parenthesis(top):
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
    s = '5+23-5-(4-2)+(3-5(3+0))-12'
    print(convert_infix_to_postfix(s))