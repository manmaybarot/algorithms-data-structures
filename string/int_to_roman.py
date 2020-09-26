# 1: 'I',
# 5: 'V',
# 10: 'X',
# 50: 'L',
# 100: 'C',
# 500: 'D',
# 1000: 'M',

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral. Input is guaranteed to
# be within the range from 1 to 3999.

# Ref: https://leetcode.com/problems/integer-to-roman/

def intToRoman(self, num: int) -> str:
        table = {
            '1000': ['', 'M', 'MM', 'MMM'],
            '100': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            '10': ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            '1': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        }

        return table['1000'][num//1000] + \
            table['100'][num % 1000 //100] + \
            table['10'][num% 100 //10 ]+ \
            table['1'][num % 10 ]