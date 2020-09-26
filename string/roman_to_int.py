# Convert roman to int

# Ref: https://leetcode.com/problems/roman-to-integer/

def romanToInt(self, s: str) -> int:
    table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = table[s[-1]]

    for i in reversed(range(len(s) - 1)):
        if table[s[i]]< table[s[i + 1]]:
            total -= table[s[i]]
        else:
            total += table[s[i]]

    return total
