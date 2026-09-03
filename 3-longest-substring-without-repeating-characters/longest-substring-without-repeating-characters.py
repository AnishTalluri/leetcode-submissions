class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        indexed_chars = {}
        left = 0

        for right in range(len(s)):
            if s[right] in indexed_chars and indexed_chars[s[right]] >= left:
                left = indexed_chars[s[right]] + 1
            indexed_chars[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
