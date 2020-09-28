# Given a string S and a string T, find the minimum window in S which
# will contain all the characters in T in complexity O(n).

# Ref: https://leetcode.com/problems/minimum-window-substring/

import collections
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        - We are decrementing t_set counter which was initially set to match
          t string's chars
        - If we decrement a char's value in t_set which is already present in
          the t, so we can ignore
          earlier occurences of that char when we strink the left pointer
        - When we srink the left pointer, we are incrementing the char value
          first in the t_set

                EX: s = 'ABAACA', t = 'AC'
        - Let say, in above when right pointer reaches to index 4, we would
          have t_set['A'] = -2
        - Means, when we start strinking/sliding left towards right, we can
          ignore first 2 'A's as we are only considering the current char as
          in calculation whose t_set val > 0
        - At first, this might seem wierd, but if we try slowely,
          it is not that hard.
        '''

        t_set = collections.defaultdict(lambda: 0)

        for i in t:
            t_set[i] += 1

        min_left, min_right = -inf, inf
        left = 0
        right = 0
        counter = 0

        while right < len(s):
            t_set[s[right]] -= 1

            if t_set[s[right]] >= 0:
                counter += 1

            if counter == len(t):
                # strip left until we can
                while t_set[s[left]] + 1 <= 0:
                    t_set[s[left]] += 1
                    left += 1

                # calculate min lenght and get new indeces
                if min_right - min_left > right - left:
                    min_left = left
                    min_right = right

                # discard currerntly considered left
                t_set[s[left]] += 1
                counter -= 1
                left += 1

            right += 1

        if min_left == -inf and min_right == inf:
            return ''

        return s[min_left: min_right + 1]
