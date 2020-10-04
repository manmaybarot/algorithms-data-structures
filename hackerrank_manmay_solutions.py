# 1.) From A to B

#
# Complete the 'a_to_b' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER x_start
#  2. INTEGER y_start
#  3. INTEGER x_end
#  4. INTEGER y_end


def a_to_b(x_start, y_start, x_end, y_end):
    '''
    Approach: Modulo Variant (Maths)
    Time Complexiy: O(log(max(x_end, y_end)))
    Space Complexiy: O(1)
    '''
    while x_end >= x_start and y_end >= y_start:
        if x_end == y_end:
            break
        elif x_end > y_end:
            if y_end > y_start:
                x_end %= y_end
            else:
                return (x_end - y_end) % y_end == 0
        else:
            if x_end > x_start:
                y_end %= x_end
            else:
                return (y_end - y_start) % x_end == 0

    return x_start == x_end and y_start == y_end


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     x_start = int(input().strip())

#     y_start = int(input().strip())

#     x_end = int(input().strip())

#     y_end = int(input().strip())

#     result = a_to_b(x_start, y_start, x_end, y_end)

#     fptr.write(str(result) + '\n')

#     fptr.close()


################################################################################

# 2.) Math Chain

class Operations:
    '''
    Approach: Object Oriented Design
    Time Complexity: O(num of operations/calls)
    Space Complexity: O(num of operations/calls)
    '''
    current = ''

    def one(self):
        Operations.current += '1'
        return self

    def two(self):
        Operations.current += '2'
        return self

    def three(self):
        Operations.current += '3'
        return self

    def plus(self):
        Operations.current += '+'
        return self

    def minus(self):
        Operations.current += '-'
        return self

    def equals(self):
        return eval(Operations.current)

class one(Operations):
    def __init__(self):
        super().one()

class two(Operations):
    def __init__(self):
        super().two()

class three(Operations):
    def __init__(self):
        super().three()



# Enter your code here such that tests in main block pass.
# if __name__ == "__main__":
#     def tests(index):
#         if index == 3:
#             return one().plus().two().equals()
#         elif index == 1:
#             return one().equals()
#         elif index == 4:
#             return one().plus().one().plus().one().plus().one().equals()
#         elif index == 0:
#             return one().minus().two().plus().one().equals()
#         elif index == 8:
#             return two().minus().two().plus().three().plus().two().plus().three().equals()

#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     index = int(input().strip())

#     result = tests(index)

#     fptr.write(str(result) + '\n')

#     fptr.close()
