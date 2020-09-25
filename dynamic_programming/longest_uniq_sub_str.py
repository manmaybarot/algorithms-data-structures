# Given a string s, find the length of the longest substring
# without repeating characters.

# Ref:
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(self, s: str) -> int:
    if not s: return 0
    cache = {}
    count = 0
    start = 0
    for current, char in enumerate(s):
        if char not in cache:
            cache[char] = current
        else:
            pre = cache[char]
            cache[char] = current
            if pre >= start:
                start = pre+ 1
        count = max(count, current - start + 1)

    return count
