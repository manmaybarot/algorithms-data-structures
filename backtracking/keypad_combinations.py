# Letter Combinations of a Phone Number
# Ref: https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        digits_len = len(digits)
        ans = []
        current_combination = []

        def find_combinations(i):
            if i == digits_len:
                ans.append(''.join(current_combination))
            else:
                for char in keypad[digits[i]]:
                    current_combination.append(char)
                    find_combinations(i + 1)
                    current_combination.pop()

        find_combinations(0)

        return ans
