# Postfix evaluation

def eval_postfix(postfix):
    oprand_stack = []

    for i in postfix:
        if i in {'+', '-', '/', '*', '^'}:
            first = float(oprand_stack.pop())
            second = float(oprand_stack.pop())
            if i == '+':
                oprand_stack.append(first+second)
            elif i == '-':
                oprand_stack.append(first-second)
            elif i == '/':
                oprand_stack.append(first/second)
            elif i == '^':
                oprand_stack.append(first**second)
            elif i == '*':
                oprand_stack.append(first*second)
        else:
            oprand_stack.append(i)

    return oprand_stack[0]


if __name__ == '__main__':
    postfix = '523+5-42-3530+^*12/-'
    print(eval_postfix(postfix))

# For prefix eval, got right to left :)
